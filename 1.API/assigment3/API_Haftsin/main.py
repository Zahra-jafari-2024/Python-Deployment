from fastapi import FastAPI, HTTPException, status
from fastapi.responses import FileResponse,StreamingResponse
from pathlib import Path
import io
import uvicorn
import cv2

app = FastAPI()

pieces = {
    "apple": {

        "image": 'image/apple.jpg',
        "des": "سیب نماد سلامتی، زندگی و زیبایی است"
    },

    "somagh": {

        "image": 'image/somagh.jpg',
        "des": "سماق نماد زیبایی و شادابی است"
    },
    "garlic": {

        "image": 'image/garlic.jpg',
        "des": "سیر نماد سلامتی و درمان بیماری‌هاست"
    },
    "coin": {

        "image": 'image/coin.jpg',
        "des": "سکه نشان‌دهنده فراوانی، برکت، توفیق و ثروت است"
    },
    "samanoo": {

        "image": 'image/samanoo.jpg',
        "des": "سمنو نماد عشق و محبت در سفره هفت سین است"
    },
    "sabzeh": {

        "image": 'image/sabzeh.jpg',
        "des": "سبزه یکی از مهم‌ترین نمادهای سفره هفت سین است که بهار و زندگی را نشان می‌ده"
    },
    "serkeh": {

        "image": 'image/serkeh.jpg',
        "des": "سرکه نماد زندگی و بردباری در برابر مشکلات محسوب می‌شود"
    }
}


@app.get("/")
def read_root():
    return "Happy new year. wellcom to my api . Its about Haftsin"


@app.get("/pieces")
def get_pieces():
    return pieces


@app.get("/pieces/{piece_name}/")
def read_piece_info(piece_name: str):
            return pieces[piece_name]["des"]


@app.get("/pieces/image")
def read_default_image():
    image2=cv2.imread(r"image/haftsin.jpg")
    _, encode_image = cv2.imencode('.jpg', image2)
    return StreamingResponse(content=io.BytesIO(encode_image.tobytes()), media_type="image/jpg")

@app.get("/pieces/image/{piece_name}")
def read_piece_image(piece_name: str):
    if piece_name == 'apple' or piece_name == 'coin' or piece_name == 'garlic' or piece_name == 'sabzeh' or piece_name == 'samanoo' or piece_name == 'serkeh' or piece_name=='somagh':
        images = pieces[piece_name]["image"]
        return FileResponse(images)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="piece name must coin or garlic or sabzeh or samanoo or serkeh or somagh or apple")