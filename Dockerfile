FROM python:3.9-alpine
WORKDIR /project
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ADD . .
#RUN pip install -r requirements.txt
WORKDIR ./controller
ENTRYPOINT ["python3"]
CMD ["app.py"]
