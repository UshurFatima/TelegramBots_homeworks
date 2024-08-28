FROM python:3.11-slim

WORKDIR /app
COPY reqs.txt /app
RUN pip install --no-cache-dir -r reqs.txt

COPY . /app

CMD ["python", "main.py"]