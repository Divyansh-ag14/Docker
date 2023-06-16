### Simple Process to dockerize flask ml apps

Test App: simple flask app to predict salary of an employee.


### Installation

To run the app, make sure to include the defined dependencies.
```bash
pip install -r requirements.txt
```

### Start the Server
```bash
python run appp.py
```

### Dockerize the app
1. Create a Dockerfile 
```bash
FROM python:3.11
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
```

2. Create an image
```bash
docker build -t testapp . 
```