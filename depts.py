from fastapi import APIRouter,HTTPException,Depends
from database import get_db
from models import DepartmentDB,EmployeeDB
from schemas import AddDepartment,UpdateDepartment
from sqlalchemy.orm import Session

router1=APIRouter(prefix='/dept',tags=['部门管理'])

@router1.get('/')
def home(db:Session=Depends(get_db)):
    success=db.query(DepartmentDB).all()
    return success
@router1.get('/{id}')
def home_id(id:int,db:Session=Depends(get_db)):
    success=db.query(DepartmentDB).filter(DepartmentDB.id==id).first()
    if success:
        return {'message':f'查找{id}部门成功','code':200,'data':success}
    raise HTTPException(status_code=404,detail='该部门未找到')
@router1.post('/')
def add_dept(add:AddDepartment,db:Session=Depends(get_db)):
    success=db.query(DepartmentDB).filter(DepartmentDB.name==add.name).first()
    if success:
        raise HTTPException(status_code=400,detail='该部门已存在，添加失败')
    new=DepartmentDB(name=add.name,location=add.location)
    db.add(new)
    db.commit()
    return {'message':f'添加{add.name}成功','code':200}
@router1.put('/{id}')
def update_dept(id:int,update:UpdateDepartment,db:Session=Depends(get_db)):
    success=db.query(DepartmentDB).filter(DepartmentDB.id==id).first()
    if success:
        success.location=update.new_location
        db.commit()
        return {'message':f'修改{id}部门的地址成功','code':200}
    raise HTTPException(status_code=404,detail='部门未找到，修改失败')
@router1.delete('/{id}')
def delete_dept(id:int,db:Session=Depends(get_db)):
    exist=db.query(EmployeeDB).filter(EmployeeDB.dept_id==id).first()
    if exist:
        raise HTTPException(status_code=400,detail='该部门还有员工无法删除')
    success = db.query(DepartmentDB).filter(DepartmentDB.id == id).first()
    if success:
        db.delete(success)
        db.commit()
        return {'message': f'删除{id}部门成功', 'code': 200}
    raise HTTPException(status_code=404, detail='部门未找到，删除失败')
