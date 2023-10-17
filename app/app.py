#!/usr/bin/env python3
from flask import Flask, make_response
from flask_migrate import Migrate
from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
migrate = Migrate(app,db)
db.init_app(app) 

@app.route('/')
def index(id):
    response_body = '<h1>Hello World</h1>'
    status = 200
    headers = {}
    return make_response(response_body,status,headers)
    # redirect


if __name__ == '__main__':
    app.run(port=5000)
