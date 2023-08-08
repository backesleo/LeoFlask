from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = "123456"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\muril\\Documents\\APEX\\LeoFlask\\aplication.sqlite3'


db = SQLAlchemy(app)

 
from view import *

if __name__ == '__main__':  
    app.run(debug=True)


