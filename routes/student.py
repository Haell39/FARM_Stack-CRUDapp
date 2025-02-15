from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity

student_router = APIRouter()

@student_router.get('/student')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())

@student_router.get('/hello')
async def hello_world():
    return "Hello World"

#creating a new student
@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())