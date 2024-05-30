# Convert an Image To a Watercolor Image 

+ Input :
<p align="center"><img src="https://github.com/Kiana-Jahanshid/picopy/raw/main/picopy/na.jpg" width="290" height="200" ></p> 

<br>

+ Output :
<p align="center"><img src="https://github.com/Kiana-Jahanshid/picopy/raw/main/picopy/watercolor.jpg" width="410" height="300" ></p>

<br/>

# Installation 

```bash
pip install picopy
```

<br>

# How to use 

## 1. Use with Python environments : 

```python
from picopy import picopy 

picopy.convert_image_to_watercolor("image.jpg")

 or 

picopy.convert_image_to_watercolor("https://..../image.jpg")
```
<br>

## 2. Use with CLI :

+ using local image :

```bash
python -m picopy.picopy --imagepath "image.jpg"
```

+ using URL :

```bash
python -m picopy.picopy --imagepath "https://..../image.jpg"
```


Your watercolored image will be saved in your file folder .
