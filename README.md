# Introduction
This Template API was created to help new developers to create a new APIs easily and with a pattern requested by the company

CreatedBy: Douglas Buss Ronchi <br>
CreationDate: 2022/04 <br>
CreaterEmail: <br>
Credits: <br>

# Getting Started
### 1. Installation process

- Clone this repo
- Run ```pip install -r requirements/dev.txt``` command
- Create a ```.env``` file with the environment variables like ```.env.example```
- Run ```nerdctl compose up -d``` command
- Start ```run.py``` file.
- It runs an uvicorn server at ```127.0.0.1:8000```
- Acess the docs from ```127.0.0.1:8000/docs```

### 2. Software dependencies
   - MongoDB

### 3. Project requirements
### Dev
- pytest==7.1.1
- pytest-cov==3.0.0
- pytest-mock==3.7.0
- pyclean==2.2.0
- mongomock==4.0.0
### App
- httpie==3.1.0
- pydantic==1.9.0
- mongoengine==0.24.1
- loguru==0.6.0
- fastapi==0.75.1
- starlette==0.17.1
- requests==2.27.1
- PyJWT==2.3.0
- uvicorn==0.17.6
- pymongo==4.1.1
    

### 4. Latest releases
- v1.0.0 - First Release

### 5. API references
- FastAPI

# Build and Test
To run the tests just follow the steps:
- Run ```pip install -r requirements/test.txt``` command
- Run ```pytest``` command

# Contribute
Feel free to contribute, just make a new branch from main branch, make the changes and open a new pull request.
