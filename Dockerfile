FROM python
COPY . /app
WORKDIR /app
RUN pip install -r requirements2.txt
ENTRYPOINT ["python"]
CMD ["helloworld.py"]