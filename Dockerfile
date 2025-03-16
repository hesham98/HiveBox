FROM python:3.9

WORKDIR /app

COPY * .

RUN apt-get update && \
    apt-get install -y curl && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["flask" , "run", "--host=0.0.0.0", "--port=5000"]