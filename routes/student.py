from fastapi import APIRouter, HTTPException
from models.student import Student
from config.database import db
from schemas.student import studentEntity, listOfStudentEntity

student_router = APIRouter(prefix="/students")

# Buscar todos os estudantes
@student_router.get('/')
async def find_all_students():
    return listOfStudentEntity(db.student.find())

# Rota de teste
@student_router.get('/hello')
async def hello_world():
    return {"message": "Hello World"}

# Criar um novo estudante
@student_router.post('/')
async def create_student(student: Student):
    new_student = dict(student)
    result = db.student.insert_one(new_student)
    new_student['_id'] = str(result.inserted_id)  # Convertendo ObjectId para string
    return studentEntity(new_student)
