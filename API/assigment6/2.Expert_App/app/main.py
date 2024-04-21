from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    yield db
    db.close()


@app.get("/students", response_model=list[schemas.Student])
def get_student_all( db: Session = Depends(get_db)):
    stu = crud.get_student_all(db)
    return stu

@app.get("/course", response_model=list[schemas.Course])
def get_course_all( db: Session = Depends(get_db)):
    cou = crud.get_course_all(db)
    return cou


@app.get("/students/{id}", response_model=schemas.Student)
def get_student_db(id:int, db:Session = Depends(get_db)):
    stu = crud.get_student(db=db, id=id)
    return stu



@app.get("/course/{id}", response_model=schemas.Course)
def get_course(id:int, db:Session = Depends(get_db)):
    cou = crud.get_course(db=db, id=id)
    return cou


@app.post("/students/", response_model=schemas.Student)
def add_student(student: schemas.StudentCreate, db:Session = Depends(get_db)):
        stu=crud.add_student(db=db, stu=student)
        return stu

@app.post("/course/", response_model=schemas.Course)
def add_course(id:int, course: schemas.CourseCreate, db:Session = Depends(get_db)):
    db_course = crud.add_course(db=db, course=course, id=id)
    return db_course

@app.put("/students/", response_model=schemas.Student)
def update_student_db(id:int, student: schemas.StudentCreate,db:Session = Depends(get_db)):
    stu = crud.update_student(db=db, id=id,upstu=student)
    return stu

@app.put("/courses", response_model=schemas.Course)
def update_course_db(id:int, course: schemas.CourseCreate, db:Session = Depends(get_db)):
    db_course = crud.update_course(id=id, db=db, course=course)
    return db_course

@app.delete("/student/{id}", response_model=schemas.Student)
def delet_student(id:int,db:Session = Depends(get_db)):
    stu=crud.del_student(db=db, id=id)
    return {"message":"Deleted Done"}

@app.delete("/courses/{id}", response_model=schemas.Course)
def delet_course(id:int, db:Session = Depends(get_db)):
    co=crud.del_course(db=db, id=id)
    return "Deleted Done"