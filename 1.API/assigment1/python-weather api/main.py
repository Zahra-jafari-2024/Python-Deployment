import json
import requests
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from requests import get as getWeather
app = QApplication([])

def forecast(self):
    cityname=ui1.lecity.text()
    url ="http://goweather.herokuapp.com/weather/"+cityname
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    if response.status_code == 200:
       weather = json.loads(response.text)
       ui1.wind_t.setText(weather["wind"])
       description = weather["description"]
       ui1.deg_t.setText(weather["temperature"])
       ui1.des_t.setText(weather["description"])
       if description == "Sunny":
         ui1.result_board_2.setIcon(QIcon("image/sunny.png"))
       elif description == "Clear":
         ui1.result_board_2.setIcon(QIcon("image/Cloudy.png"))
       elif description == "Partly cloudy":
         ui1.result_board_2.setIcon(QIcon("image/partlycloudy.png"))
       elif description == "Rainny":
         ui1.result_board_2.setIcon(QIcon("image/rainy.png"))
       elif description == "Light rain, mist":
         ui1.result_board_2.setIcon(QIcon("mage/sr.png"))
       else:
         ui1.result_board_2.setIcon(QIcon("image/sunny.png"))

       temp = weather.get("forecast")
       weather1 = temp[0]
       weather2 = temp[1]
       weather3 = temp[2]
       ui1.temp1.setText("temperature :" + weather1.get("temperature"))
       ui1.wind1.setText("wind :" + weather1.get("wind"))
       ui1.temp2.setText("temperature :" + weather2.get("temperature"))
       ui1.wind2.setText("wind :" + weather2.get("wind"))
       ui1.temp3.setText("temperature :" + weather3.get("temperature"))
       ui1.wind3.setText("wind :" + weather3.get("wind"))
    else:
       print("error")
loader = QUiLoader()
ui1 = loader.load("mail.ui")
ui1.show()
ui1.pushButton.clicked.connect(forecast)
app.exec()




