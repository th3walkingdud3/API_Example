FROM python:3.9.10-slim-bullseye
COPY . ~/
WORKDIR ~/
RUN apt-get update && pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["uvicorn","main:app","--reload","--host","0.0.0.0"]
