import  streamlit as st
import  easyocr
import cv2
from fastapi import FastAPI,File,Form,UploadFile,HTTPException
from fastapi.responses import StreamingResponse
import numpy as np

app=FastAPI()

@app.get("/")
def read_root():
    return "EasyOCR is a deep learning-based optical character recognition (OCR) method used for recognizing and extracting characters from images, particularly number plates"

@app.post("/image_processing/")
async def image_processing(input_file:UploadFile=File(None)):
        if not input_file.content_type.startswith("image/"):
                 raise HTTPException(status_code=415,detail="unsupported file type")
        contents=await input_file.read()
        np_arry=np.frombuffer(contents,dtype=np.uint8)
        image=cv2.imdecode(np_arry,cv2.IMREAD_UNCHANGED)
        cv2.imwrite("test.jpg",image)
        reader = easyocr.Reader(['fa', 'en'])
        result = reader.readtext('test.jpg', detail=0, paragraph=True)
        print(result)
        return(result)

