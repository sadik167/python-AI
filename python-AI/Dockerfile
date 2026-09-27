FROM python
WORKDIR /app
COPY requiremts.txt .
RUN pip install -r requiremts.txt
COPY app.py .
EXPOSE 9090
ENTRYPOINT [ "python","app.py" ]