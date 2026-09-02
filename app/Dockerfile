FROM python:3.12-alpine
RUN apk update && apk upgrade
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
EXPOSE 5050
CMD ["python", "main.py"]
