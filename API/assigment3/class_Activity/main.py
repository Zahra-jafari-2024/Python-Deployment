import cv2
from fastapi import FastAPI
import numpy
import cv2
import io
from fastapi.responses import StreamingResponse
app=FastAPI()

@app.get("/")
def tab1():
 return {"hello":"world"}

@app.get("/item/{itemid}")
def tab2(itemid:int,q=None):
   return{"itemid":itemid ,"q": q}

@app.get("/salam")
def tab3():
     return "علیک سلام "
@app.get("/salam/{user}")
@app.get("/salam/{user}/{family}")
def tab4(user : str,family : str="jafari"):
    return {"علیک سلام  " +user+" "+family+"چانم"}

@app.get("/imagec")
def image_c():
  image=cv2.imread(r"1.png")
  _,enc=cv2.imencode(".png",image)
  return StreamingResponse(content=io.BytesIO(enc.tobytes()),media_type="image/png")