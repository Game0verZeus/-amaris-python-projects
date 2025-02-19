from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on AWS Lambda!"}

# We create a handler for AWS Lambda using Mangum
handler = Mangum(app)
=======
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on AWS Lambda!"}

# We create a handler for AWS Lambda using Mangum
handler = Mangum(app)

