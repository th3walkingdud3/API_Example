FROM python:3.11.0a4-slim
COPY . ~/
WORKDIR ~/
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["uvicorn","main:app","--reload","--host","0.0.0.0"]
