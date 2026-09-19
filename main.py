from fastapi import FastAPI
from database import engine,Base
from routers.depts import router1
from routers.emps import router2

app=FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router1)
app.include_router(router2)
if __name__=='__main__':
    import uvicorn
    uvicorn.run(app,host='127.0.0.1',port=8000)