FROM python:3.13-alpine

RUN apk add --no-cache bash && \
    addgroup -S flask-app-group && \
    adduser -S flask-app-user -G flask-app-group

WORKDIR /app

COPY --chown=flask-app-user:flask-app-group . /app 

USER flask-app-user

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
