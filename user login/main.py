from flask import Flask, request, render_template
import mysql.connector
import re
app=Flask(__name__)
@app.route("/login")
def l():
    msg=""
    if(request.method=="POST" and "username" in username and "password" in password):
        username=request.form.get("username")
        password=request.form.get("password")
        d=mysql.connector.connect(
            host= "sql12.freesqldatabase.com"
            name= "sql12784240"
            username= "sql12784240"
            password= "lUxmX5H2Vd"

        )

        cursor=d.cursor()
        cursor.execute("SELECT * FROM logindata WHERE NAME=%s AND PASSWORD=%s", (username, password))
        account=mysql.fetchone()
        if account:
            print("Logged in successfully")
            name=account[0]
            id=account[1]
            print("log in done")
            msg="Logged in "
            return render_template("login.html",msg=msg, name=name, id=id)
        
        else:
            print("invalid details")
            msg="log in unsuccessful"
            return render_template("login.html", msg=msg)
        
    else:
        return render_template("login.html")
    
@app.route("/logout")
def logout():
    name=""
    id=""
    msg="logged out successfully"
    return render_template("login.html",msg=msg, name=name, id=id)

@app.route("/register", methods=["GET, POST"])
def register():
    if request.method=="POST" and "username" in request.form and "password" in request.form and "email" in request.form:
        username=request.form["username"]
        password=request.form["password"]
        email=request.form["email"]
        d=mysql.connector.connect(
             host= "sql12.freesqldatabase.com"
            name= "sql12784240"
            username= "sql12784240"
            password= "lUxmX5H2Vd"
        )
        mycursor=d.cursor
        print(username)

        mycursor.execute(
            "SELECT * FROM logindata WHERE USERNAME=%s AND EMAIL_ID =%s",(username, email)
        )

        account=mycursor.fetchone()
        print(account)

        if account:
            msg="account already exists"

        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):

            msg = 'Invalid email address !'

        elif not re.match(r'[A-Za-z0-9]+', username):
            msg="useranme must contain only chararecters and numbers"

        elif not username or not password or not email:
            msg="Kindly fill the details"

        else:
            mycursor.execute("INSERT INTO logindata values(%s,%s,%s)",(username, email, password))

            d.commit()
            msg="log in successful"
            name=username
            return render_template("index.html", msg=msg, name=name)
        
    elif request.method=="POST":
        msg="kindly fill the details"
    return render_template("register.html", msg=msg)

@app.route("/", methods=["GET","POST"])

def index():
    return render_template("login.html")

app.run(host="0.0.0.0", port=8080)



