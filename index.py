#import statements
from fastapi import FastAPI
from routes.student import student_router

#Creating app

app = FastAPI()

#Including routers
app.include_router(student_router)

