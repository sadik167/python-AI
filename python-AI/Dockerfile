FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 9090
ENTRYPOINT [ "python","app.py" ]
