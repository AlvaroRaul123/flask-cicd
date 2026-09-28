FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt app.py ./
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]

