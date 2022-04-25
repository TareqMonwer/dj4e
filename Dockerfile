FROM python:3.10.4-alpine

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/
COPY entrypoint.sh /app/

RUN ["chmod", "+x", "/app/entrypoint.sh"]
RUN pip install -r requirements.txt

COPY . /app/
ENTRYPOINT ["sh", "/app/entrypoint.sh"] 

