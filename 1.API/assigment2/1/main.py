import json
import requests
import tkinter
from tkinter import messagebox
import dotenv
import os
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
import urllib.request
app = QApplication([])

def display(self):
    name=ui1.name.text()
    pattern=ui1.url.text()
    dotenv.load_dotenv()
    api_illusion = os.getenv("api_illusion")
    url = "https://54285744-illusion-diffusion.gateway.alpha.fal.ai/"
    payload = {
    "image_url": pattern,
    "prompt": "(masterpiece:1.4), (best quality), (detailed), landscape,"+name,
    "negative_prompt": "(worst quality, poor details:1.4), lowres, (artist name, signature, watermark:1.4), bad-artist-anime, bad_prompt_version2, bad-hands-5, ng_deepnegative_v1_75t"
    }
    # Status Code 401 - Unauthorized
    headers = {
        "Authorization": api_illusion,
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)
    print(response.text)
    # response1=response.json()["image"]
    # m=str(response1["url"])
    # print(m)
    urllib.request.urlretrieve(response.json()["image"]["url"],"generated_img.jpg")
    # ui1.pushButton_3.setIcon(QIcon("generated_img.jpg"))
    pixmap = QPixmap("generated_img.jpg")
    ui1.label_3.setPixmap(pixmap)
def plan(self):
    api_key = os.getenv("api_key")
    url = "http://my-api.plantnet.org/v2/identify/all"
    payload = {
        "api-key":  api_key
    }
    FILES = {
        "images": open("generated_img.jpg", "rb")
    }
    response = requests.post(url, params=payload, files=FILES)
    print(response.status_code)
    # name=response.json()["results"][0]["species"]["commonNames"]
    # msgBox = QMessageBox()
    # msgBox.setText(name)
    # msgBox.exec_()
    print(response.text)
    print(response.json()["results"][0]["species"]["genus"]["scientificName"])
    ui1.lineEdit.setText(response.json()["results"][0]["species"]["genus"]["scientificName"])




loader = QUiLoader()
ui1 = loader.load("untitled.ui")
ui1.show()
def url1():
    ui1.url.setText("https://storage.googleapis.com/falserverless/illusion-examples/funky.jpeg")
def url2():
    ui1.url.setText("https://storage.googleapis.com/falserverless/illusion-examples/checkers.png")
def url3():
    ui1.url.setText("https://storage.googleapis.com/falserverless/illusion-examples/ultra_checkers.png")

ui1.result_board_2.setIcon(QIcon("image/1.png"))
ui1.result_board_3.setIcon(QIcon("image/2.png"))
ui1.result_board_4.setIcon(QIcon("image/3.png"))
ui1.pushButton.clicked.connect(display)
ui1.pushButton_2.clicked.connect(plan)
ui1.result_board_2.clicked.connect(url1)
ui1.result_board_3.clicked.connect(url2)
ui1.result_board_4.clicked.connect(url3)


app.exec()
