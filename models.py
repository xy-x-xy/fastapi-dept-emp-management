from sqlalchemy import Column,Integer,Float,String
from database import Base

class DepartmentDB(Base):
    __tablename__='dept'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(20),unique=True,nullable=False)
    location=Column(String(20),nullable=False)

class EmployeeDB(Base):
    __tablename__='employee'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(20),nullable=False)
    age=Column(Integer,nullable=False)
    salary=Column(Float,nullable=False)
    dept_id=Column(Integer,nullable=False)
