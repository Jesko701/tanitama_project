from dotenv import load_dotenv
from flask import Flask, jsonify, request
from database.UserModel import init_app
from controller.UserController import UserController
from controller.Authorization import required_token

import os
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('database_uri')
app.config['SECRET_KEY'] = os.getenv("secret_key")

init_app(app)
user_controller = UserController()

@app.route('/users', methods=['GET'])
@required_token
def get_all_users():
    return user_controller.getAll()

@app.route('/users', methods=['POST'])
def create_user():
    username= request.json['username']
    email=request.json['email']
    password=request.json['password']
    confirm_password=request.json['confirm_password']
    return UserController.createUser(self=UserController,username=username,email=email,password=password,confirmPass=confirm_password)

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    pw = request.json['password']
    return user_controller.loginUser(username=username,password=pw)

    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='8000', debug='True')
else:
    print("Tidak bisa menjalankan program ini")