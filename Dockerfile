  
FROM python:3.9.4
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY main.py .
EXPOSE 5000
CMD ["python", "./main.py"]

