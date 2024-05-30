from fastapi import FastAPI, Form, HTTPException
import sqlite3

app = FastAPI()

@app.get("/")
def read_root():
    return "Wellcom to ToDo API Application"


@app.get("/item")
def read_task():
    connection = sqlite3.connect("app/todo.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    results = cursor.fetchall()
    return results


@app.post("/item")
def add_task(id:int = Form(), title:str = Form(), description:str = Form(), time:str = Form(), status:int = Form()):
    connection = sqlite3.connect("app/todo.db")
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO tasks(id, title, description, time, status) VALUES("{id}","{title}","{description}","{time}","{status}")')
    connection.commit()
    return "Added Done"


@app.delete("/item/{id}")
def delete_task(id:int):
    connection = sqlite3.connect("app/todo.db")
    cursor = connection.cursor()
    cursor.execute("SELECT count(id) FROM tasks where id='{id}'")
    results = cursor.fetchall()
    row_count=results[0]
    if row_count==0:
            raise HTTPException(status_code=404,detail="item not found")
    cursor.execute(f'DELETE FROM tasks WHERE id="{id}"')
    connection.commit()
    return "Deleted Done"


@app.put("/item/{id}")
def edit_task(id:int,title:str = Form(None), description:str = Form(None), time:str = Form(None), status:int = Form(None)):
    connection = sqlite3.connect("app/todo.db")
    cursor = connection.cursor()
    if title or description or time or status is None:
        raise HTTPException(status_code=204, detail="Please complete the information")
    else:
        cursor.execute(f'UPDATE tasks SET title="{title}", description="{description}", time="{time}", status="{status}" WHERE id="{id}"')
        connection.commit()
        return "Edited Done"
    