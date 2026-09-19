from fastapi import APIRouter,HTTPException,Depends
from database import get_db
from models import DepartmentDB,EmployeeDB
from schemas import AddEmployee,UpdateEmployee
from sqlalchemy.orm import Session

router2=APIRouter(prefix='/emp',tags=['员工管理'])

@router2.get('/')
def home_emp(db:Session=Depends(get_db)):
    success=db.query(EmployeeDB).all()
    return success
@router2.get('/{id}')
def home_id(id:int,db:Session=Depends(get_db)):
    success=db.query(EmployeeDB).filter(EmployeeDB.id==id).first()
    if success:
        return {'message':f'查找{id}员工成功','code':200,'data':success}
    raise HTTPException(status_code=404,detail='该员工未找到')
@router2.post('/')
def add_emp(add:AddEmployee,db:Session=Depends(get_db)):
    exist=db.query(DepartmentDB).filter(DepartmentDB.id==add.dept_id).first()
    if exist:
        success = db.query(EmployeeDB).filter(EmployeeDB.name == add.name).first()
        if success:
            raise HTTPException(status_code=400, detail='该员工已存在,添加失败')
        new = EmployeeDB(name=add.name, age=add.age, salary=add.salary, dept_id=add.dept_id)
        db.add(new)
        db.commit()
        return {'message': f'添加{add.name}员工成功', 'code': 200}
    raise HTTPException(status_code=404,detail='无部门号可选')
@router2.put('/{id}')
def update_emp(id:int,update:UpdateEmployee,db:Session=Depends(get_db)):
    success=db.query(EmployeeDB).filter(EmployeeDB.id==id).first()
    if success:
        success.salary=update.new_salary
        db.commit()
        return {'message':f'修改{id}员工工资成功','code':200}
    raise HTTPException(status_code=404,detail='该员工未找到，修改失败')
@router2.delete('/{id}')
def delete_emp(id:int,db:Session=Depends(get_db)):
    success=db.query(EmployeeDB).filter(EmployeeDB.id==id).first()
    if success:
        db.delete(success)
        db.commit()
        return {'message':f'删除{id}员工成功','code':200}
    raise HTTPException(status_code=404,detail='员工未找到，删除失败')