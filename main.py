
from flask import Flask,render_template,request
import mysql.connector

app=Flask(__name__)

conn=mysql.connector.connect(host="remotemysql.com",user="hmNqvVUT8d",password="Wz7BTOmyqc",database="hmNqvVUT8d")
cursor=conn.cursor()

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login_validation',methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        return render_template('home.html')
    else:
        return render_template('login.html')
    #return users

@app.route('/app_user',methods=['POST'])
def add_user():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')
    cursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`password` VALUES(NULL,'{}','{}','{}')""".format(name,email,password))
    conn.comit()
    return "Sucessfull"
 

if __name__=="__main__":
    app.run(debug=True)