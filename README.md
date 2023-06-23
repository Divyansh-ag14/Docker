### Simple Process to dockerize flask ml apps

Test App: simple flask app to predict salary of an employee.


### Installation

To run the app, make sure to include the defined dependencies.
```bash
pip install -r requirements.txt
```

### Start the Server
```bash
python run app.py
```

### Dockerize the app
To download Docker [click here](https://www.docker.com/products/docker-desktop/)

<br>1. Create a Dockerfile (make sure you have docker installed)<br>
In your code base create a file named "Dockerfile"
```bash
FROM python:3.11
(Use the official Python 3.11 base image as the starting point for our container.)

COPY . .
(Copy the entire current directory into the container.)

RUN pip install -r requirements.txt
(Install the Python dependencies specified in the requirements.txt file.)

EXPOSE 80
(Expose port 80 on the container, allowing external access to our application.)

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
(Set the command to be executed when the container starts. Here, we use Flask to run our application
 with the specified host and port, allowing it to be accessed externally.)

```

<br>More explanation for the above file:
1. FROM python:3.11
<br>This line specifies the base image for the Docker container. In this case, it is the Python 3.11 image. This means the container will have Python 3.11 installed as the base environment. 

2. COPY . .
<br>This line copies the contents of the current directory (the directory where the Dockerfile is located) to the current working directory of the container. The . represents the current directory.

3. RUN pip install -r requirements.txt
<br>This line executes a command during the build process. It installs the dependencies listed in the requirements.txt file using pip, the Python package installer. The requirements.txt file typically contains a list of required Python packages and their versions.

4. EXPOSE 80
This line informs Docker that the container will listen on port 80 at runtime. It exposes port 80 to allow communication with the container's processes using that port. However, it doesn't actually publish the port to the host machine.

5. CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
This line specifies the command that will be executed when the container is run. It launches the Flask application using the flask run command with additional options. It sets the host to 0.0.0.0 to listen on all available network interfaces and the port to 80.

<br>2. Create an image (make sure you are in your project directory)<br>
Write the below command on terminal
```bash
docker build -t testapp . 
```

<br>3. Check the newly built image
```bash
docker images
```
<img src = "./image.png">

<br>4. Run the container
```bash
docker run -p 80:80 testapp
```

<br>5. Push the image to docker hub <br>
1. first, tag the image according to the naming convention<br>
```bash
docker tag testapp YOUR-USER-NAME/testapp
```

2. Now, push it to docker hub

```bash
docker push YOUR-USER-NAME/testapp
```