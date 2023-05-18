# Docker file allows us to build one service

# Operating system
FROM python:3.8-slim-buster

# Ensure python output is send straight in terminal - container log
ENV PYTHONUNBUFFERED=1

# Working directory - install everything in the container in the folder
WORKDIR /django

# Copy file
COPY requirements.txt requirements.txt

# Install it
RUN pip3 install -r requirements.txt

# After dockerfile
# Docker compose - we are composing multiple services
# Yaml - data serialization language

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]