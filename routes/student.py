from fastapi import APIRouter, HTTPException, status
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

student_router = APIRouter()

@student_router.get('/hello')
async def hello_world():
    return "Hello World"

@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId: str):
    return studentEntity(connection.local.student.find_one({'_id': ObjectId(studentId)}))
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())

@student_router.post('/students')
async def create_student(student: Student):
    # connection.local.student.insert_one(dict(student)) # -- dict(student) is deprecated
    connection.local.student.insert_one(student.model_dump())

    return listOfStudentEntity(connection.local.student.find())

@student_router.put('/students/{studentId}')
async def update_student(studentId: str, student: Student):
    connection.local.student.find_one_and_update(
        {'_id': ObjectId(studentId)},
        {
            '$set': student.model_dump()  # convert student to dictionary
        }
    )

    return studentEntity(connection.local.student.find_one({'_id': ObjectId(studentId)}))

@student_router.delete('/students/{studentId}')
async def delete_student(studentId: str):
    deleted_object = connection.local.student.find_one_and_delete({'_id': ObjectId(studentId)})

    # Check if the document was actually found and deleted
    if deleted_object is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {studentId} not found"
        )

    return studentEntity(deleted_object)
