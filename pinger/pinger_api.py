from messaging.task_logger import DefaultTaskLogger, Logger
from sys import platform
import subprocess

import re

# from pinger.models import PingerParse
from typing_extensions import TypedDict

class PingerParse(TypedDict):
    ping_sent: int
    ping_rcv: int
    prc_lost: int
    time_avg: float
    status: str

class Pinger:
    def __init__(
        self, windfarm_name = None,
        logger: Logger = None,
    ):
        self.logger = logger if logger else DefaultTaskLogger()
        self.windfarm_name = windfarm_name
        self.ping_results = []

    def ping_host(self, host: str):
        task_cli = f'ping -n {host}'
        ret = subprocess.Popen(task_cli, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ping_result, ping_error = ret.communicate()
        ping_result_parsed = self.parse_result(ping_result, self.logger)
        return ping_result_parsed

    def store_ping_results(self):
        pass

    def run_pinger_api(self):
        self.logger.info('Can execute pinger api.')
        print('Can execute pinger api!')
        ping_result = self.ping_host(host="212.77.98.9")
        print(ping_result)
        self.store_ping_results()

windows_success_pattern = re.compile(
    r'\s+Packets: Sent = (?P<ping_sent>\d+), Received = (?P<ping_received>\d+), '
    r'Lost = (?P<ping_lost>\d+) \((?P<ping_percent_lost>\d+)% loss\),\s+'
    r'Approximate round trip times in milli-seconds:\s+'
    r'Minimum = (?P<time_min>[\d.]+)[ms]+, Maximum = (?P<time_max>[\d.]+)[ms]+, Average = (?P<time_avg>[\d.]+)[ms]+\s+'
)

windows_fail_pattern = re.compile(
    r'\s+Packets: Sent = (?P<ping_sent>\d+), Received = (?P<ping_received>\d+), '
    r'Lost = (?P<ping_lost>\d+) \((?P<ping_percent_lost>\d+)% loss\),'
)



def parse_result(ping_cmd_result: str, logger: Logger) -> PingerParse:
    match_patterns = []
    if _get_platform() == 'win32':
        match_patterns.append((windows_success_pattern, success_match))
        match_patterns.append((windows_fail_pattern, fail_match))
    for match_pattern, callback in match_patterns:
        match = re.search(match_pattern, ping_cmd_result)
        if match:
            return callback(match, logger)
    raise ValueError("No matching expression")

def fail_match(match, logger) -> PingerParse:
    try:
        time_avg = float(match.group('time_avg'))
    except IndexError:
        time_avg = 0

    return {
        'ping_sent': int(match.group('ping_sent')),
        'ping_rcv': int(match.group('ping_received')),
        'prc_lost': int(match.group('ping_percent_lost')),
        'time_avg': time_avg,
        'status': 'Offline'
    }

def success_match(match, logger) -> PingerParse:
    return {
        'ping_sent': int(match.group('ping_sent')),
        'ping_rcv': int(match.group('ping_received')),
        'prc_lost': int(match.group('ping_percent_lost')),
        'time_avg': float(match.group('time_avg')),
        'status': 'Online'
    }
def _get_platform():
    return platform
