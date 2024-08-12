# Official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy current directory contents into the container
COPY . /app

# Install requirements
RUN pip install -r requirements.txt

# Make port 5000 available
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py
CMD ["python", "app.py"]