FROM python:3.9

WORKDIR /app

COPY appVersion.py .

CMD ["python" , "appVersion.py"]