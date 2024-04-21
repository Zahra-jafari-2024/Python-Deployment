from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

def get_student(db: Session, id: int):
    student =  db.query(models.Student).filter(models.Student.id == id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student Not Found")
    return student


def get_student_all(db: Session):
    students =  db.query(models.Student).all()
    return students

def get_course_all(db: Session):
    courses =  db.query(models.Course).all()
    return courses

def get_course(db:Session, id:int):
    course = db.query(models.Course).filter(models.Course.id == id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course Not Found")
    return course



def add_student(db:Session,stu: schemas.StudentCreate):
     st=models.Student(firstname=stu.firstname, lastname=stu.lastname, average=stu.average, graduated=stu.graduated)
     db.add(st)
     db.commit()
     db.refresh(st) 
     return st 

def add_course(db:Session, course: schemas.CourseCreate, id:int):
    db_course = models.Course(name=course.name,unit=course.unit,owner_id=id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def update_student(db:Session,upstu: schemas.StudentCreate,id:int):
    student = db.query(models.Course).filter(models.Course.id == id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="student Not Found")
    student.firstname=upstu.firstname
    student.lastname=upstu.lastname
    student.average=upstu.average
    student.graduated=upstu.graduated
    db.commit()
    db.refresh(student)
    return student

def update_course(id:int, db:Session, course: schemas.CourseCreate):
    db_course = db.query(models.Course).filter(models.Course.id==id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course Not Found")
    db_course.name = course.name
    db_course.unit = course.unit
    db.commit()
    db.refresh(db_course)
    return db_course

def del_student(db: Session, id: int):
    student =  db.query(models.Student).filter(models.Student.id == id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student Not Found")
        
    student1 =  db.query(models.Course).filter(models.Course.owner_id == id).first()    
    if student1 is not None:
        raise HTTPException(status_code=404, detail="You Cant Delete")
    db.delete(student)
    db.commit()
    return None
     

def del_course(db: Session, id: int):
    course =  db.query(models.Course).filter(models.Course.id == id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="course Not Found")
    db.delete(course)
    db.commit()
    return None
