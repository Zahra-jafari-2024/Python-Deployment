FROM python

EXPOSE 8501

COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt

COPY . .
WORKDIR /app

ENTRYPOINT ["streamlit", "run", "app.main:app", "--server.port=8501", "--server.address=0.0.0.0"]