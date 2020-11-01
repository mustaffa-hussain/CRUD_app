FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt 
EXPOSE 5010
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
