
# Use the official Python image as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install Flask==2.3.3 \
                SQLAlchemy==2.0.21 \
                Flask-Migrate==4.0.5 \
                Werkzeug==2.3.7 \
                psycopg2-binary

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run login.py when the container launches
CMD ["python", "loginpage.py"]

