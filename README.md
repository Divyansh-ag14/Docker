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
This line specifies the base image for the Docker container. In this case, it is the Python 3.11 image. This means the container will have Python 3.11 installed as the base environment. 

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