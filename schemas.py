from pydantic import BaseModel,Field

class AddDepartment(BaseModel):
    name:str=Field(min_length=2,max_length=20)
    location:str=Field(min_length=2,max_length=20)

class UpdateDepartment(BaseModel):
    new_location:str=Field(min_length=2,max_length=20)


class AddEmployee(BaseModel):
    name:str=Field(min_length=2,max_length=20)
    age:int=Field(ge=18,le=60)
    salary:float=Field(ge=0)
    dept_id:int=Field(ge=1)
class UpdateEmployee(BaseModel):
    new_salary:float=Field(ge=0)