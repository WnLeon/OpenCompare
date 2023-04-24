from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from conf import dbconf
from module.storage.db import opencompare
from module.dbs import db

app = Flask(__name__)
app.config.from_object(dbconf)
db.init_app(app)

@app.route('/login')
def get_user():
    # Query the database to get the user info
    users = opencompare.User.query.all()
    # urls = [{image.title: image.url} for image in images]
    names = [user.name for user in users]
    password = [user.password for user in users]
    # Return the image URLs as a JSON response
    return jsonify({'users': names})
    #return jsonify({'images': urls})

@app.route('/register')
def get_images():
    # Query the database to get the image URLs
    images = opencompare.Image.query.all()
    # urls = [{image.title: image.url} for image in images]
    urls = [image.url for image in images]
    # Return the image URLs as a JSON response
    return jsonify({'images': urls})
    #return jsonify({'images': urls})