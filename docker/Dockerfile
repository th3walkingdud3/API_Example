FROM python:3.9.10-slim-bullseye
RUN apt-get update && pip install -r requirements.txt
COPY . ~/
WORKDIR ~/
EXPOSE 8000
ENTRYPOINT ["uvicorn","main:app","--reload","--host","0.0.0.0"]
