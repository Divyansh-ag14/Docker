# Set the base image to Python 3.11
FROM python:3.11

# Copy the contents of the current directory to the container's working directory
COPY . .

# Install the dependencies listed in requirements.txt using pip
RUN pip install -r requirements.txt

# Expose port 80 to allow communication with the container's processes
EXPOSE 80

# Specify the command to run when the container starts, launching the Flask application on port 80
# The --host=0.0.0.0 flag allows connections from any IP address
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]