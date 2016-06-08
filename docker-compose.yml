web:
    #restart: always
    build: .
    #command: python -u /flask_compose/app/app.py
    #command: /usr/local/bin/gunicorn -w4 -b0.0.0.0:5000 app:app
    command: /usr/local/bin/gunicorn -w4 -b0.0.0.0:5000 app:app --chdir /flask_compose/app
    ports:
        - "5000:5000"
    volumes:
        - .:/flask_compose
    links:
        - mongo
        - redis
        - mysql
    hostname: myappserver

mongo:
    image: mongo:3.0.2

redis:
    image: redis

mysql:
  hostname: mysqlserver
  image: orchardup/mysql
  environment:
     MYSQL_ROOT_PASSWORD: p@ssw0rd123
     MYSQL_DATABASE: wordpress
