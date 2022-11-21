FROM python:3.9-alpine
#WORKDIR /project
COPY . /opt/
RUN pip install -r /opt/requirements.txt
EXPOSE 5000
CMD ["python","/opt/app.py"]
