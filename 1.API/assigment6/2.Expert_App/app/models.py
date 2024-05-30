from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Float
from sqlalchemy.orm import relationship
from .database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    average = Column(Float)
    graduated = Column(Boolean)

    rel1 = relationship("Course",back_populates="rel2")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    unit = Column(Integer)
    owner_id = Column(Integer, ForeignKey("students.id"))

    rel2 = relationship("Student",back_populates="rel1")




