from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import  create_engine, MetaData
import random
from faker import Faker
from datetime import date, timedelta


# Utwórz instancję Faker
fake = Faker()

# Utwórz silnik bazy danych

Base = declarative_base()

class Group(Base):
    __tablename__ = 'Groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String(50))
    year = Column(Integer)

    students = relationship("Student", back_populates="group")

class Student(Base):
    __tablename__ = 'Students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    group_id = Column(Integer, ForeignKey('Groups.id'))

    group = relationship("Group", back_populates="students")

class Lecturer(Base):
    __tablename__ = 'Lecturers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

class Subject(Base):
    __tablename__ = 'Subjects'

    id = Column(Integer, primary_key=True)
    subject_name = Column(String(100))
    lecturer_id = Column(Integer, ForeignKey('Lecturers.id'))

    lecturer = relationship("Lecturer", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")

class Grade(Base):
    __tablename__ = 'Grades'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('Students.id'))
    subject_id = Column(Integer, ForeignKey('Subjects.id'))
    group_id = Column(Integer)
    grade = Column(Float)
    date_given = Column(Date)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")

# Utwórz tabele w bazie danych
#Base.metadata.create_all(engine)
engine = create_engine('sqlite:///example4.db', echo=True)
metadata = MetaData()


# Define all your tables before calling create_all
metadata.create_all(engine)

# Połącz się z bazą danych
#from sqlalchemy.orm import sessionmaker


# Wypełnij tabelę 'Groups'
