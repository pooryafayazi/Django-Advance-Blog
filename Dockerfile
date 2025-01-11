FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# RUN mkdir /app

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

RUN pip3 install --upgrade pip
# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application code
COPY ./core /app


# Command to run the application