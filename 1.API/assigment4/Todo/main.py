from fastapi import FastAPI,File,Form,UploadFile,HTTPException
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import io

import pyodbc


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=127.0.0.1;'
                      'Database=todo.db;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
app=FastAPI()


@app.get("/")
def root():
    return("Hi Wellcome to Api")

@app.get("/items")
def read_data():
    data={}
    j=0
    cursor.execute('SELECT * FROM tasks order by id')
    for i in cursor:
        data[j]=i
        j=j+1
    return(str(data))

@app.post("/add")
def add(title:str= Form(), description : str=Form(),time : str=Form(),status : int=Form()):
    cursor.execute(f"insert into tasks (title,description,time,status) values ('{title}','{description}','{time}','{status}')")
    conn.commit()
    data = {}
    j = 0
    cursor.execute('SELECT * FROM tasks order by id')
    for i in cursor:
        data[j] = i
        j = j + 1
    return (str(data))

@app.put("/update/{id}")
def update(id:str,title: str=Form(),description:str=Form(),time:str=Form(),status:int=Form()):
    cursor.execute('SELECT COUNT(id) FROM tasks  where id=' + id)
    result = cursor.fetchone()
    row_count = result[0]
    if row_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    sql_command = ("UPDATE tasks SET title = ?,description=?,time=?,status=? WHERE id =?")
    val = (title, description, time, status, id)
    cursor.execute(sql_command, val)
    conn.commit()
    data = {}
    j = 0
    cursor.execute(f"SELECT * FROM tasks where id={id}")
    for i in cursor:
      data[j] = i
      j = j + 1
    return (str(data))

@app.delete("/del/{id}")
def del1(id : str):
    cursor.execute('SELECT COUNT(id) FROM tasks  where id=' + id)
    result = cursor.fetchone()
    row_count = result[0]
    if row_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    cursor.execute(f"delete from tasks where id='{id}'")
    conn.commit()
    data = {}
    j = 0
    cursor.execute(f"SELECT * FROM tasks ")
    for i in cursor:
        data[j] = i
        j = j + 1
    return (str(data))









