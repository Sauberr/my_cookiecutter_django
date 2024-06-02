# Pull official base Python Docker image
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /{{cookiecutter.project_name}}
EXPOSE 8000

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /{{cookiecutter.project_name}}/
RUN pip install -r requirements.txt

# Copy the Django project
COPY . /{{cookiecutter.project_name}}/

# Add a non-root user
RUN adduser --disabled-password sauberr-user

# Switch to the non-root user
USER sauberr-user