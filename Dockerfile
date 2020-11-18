# Dockerfile

# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR .
COPY . /src/
# Install dependencies
VOLUME /media

COPY ./images/* /media/
RUN pip install -r src/requirements.txt
# RUN python src/manage.py makemigrations
# RUN python src/manage.py migrate
CMD []
# Copy project
