FROM python:3.9.18-slim

WORKDIR /workspace

COPY requirements.txt requirements.txt

COPY newgcs.json ./

RUN pip install -r requirements.txt

COPY . ./

ENV HOST 0.0.0.0

ENV GOOGLE_APPLICATION_CREDENTIALS newgcs.json

EXPOSE 8080

CMD ["python", "main.py"]