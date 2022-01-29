FROM python:3.8.0-slim
COPY . ~/
WORKDIR ~/
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["uvicorn","main:app","--reload","--host","0.0.0.0"]
