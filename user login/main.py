from flask import Flask, request, render_template
import mysql.connector
import re
app = Flask(__name__)

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def l():
    msg = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Make sure values are provided
        if username and password:
            d = mysql.connector.connect(
                host="sql12.freesqldatabase.com",
                user="sql12785113",  # Corrected from 'username'
                password="XLflfuM6vg",
                database="sql12785113"  # Corrected from 'name'
            )
            cursor = d.cursor()
            cursor.execute("SELECT * FROM logindata WHERE NAME=%s AND PASSWORD=%s", (username, password))
            account = cursor.fetchone()

            if account:
                msg = "Logged in"
                name = account[0]
                id = account[1]
                return render_template("login.html", msg=msg, name=name, id=id)
            else:
                msg = "Invalid login credentials"
    return render_template("login.html", msg=msg)

# LOGOUT
@app.route("/logout")
def logout():
    msg = "Logged out successfully"
    return render_template("login.html", msg=msg, name="", id="")

# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

        if username and password and email:
            d = mysql.connector.connect(
                host="sql12.freesqldatabase.com",
                user="sql12785113",
                password="XLflfuM6vg",
                database="sql12785113"
            )
            mycursor = d.cursor()

            mycursor.execute("SELECT * FROM logindata WHERE username=%s OR email=%s", (username, email))
            account = mycursor.fetchone()

            if account:
                msg = "Account already exists"
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = "Invalid email address!"
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = "Username must contain only letters and numbers"
            else:
                mycursor.execute("INSERT INTO logindata(username, email, password) VALUES (%s, %s, %s)", (username, email, password))
                d.commit()
                msg = "Registration successful"
                return render_template("index.html", msg=msg, name=username)
        else:
            msg = "Please fill in all fields"
    return render_template("register.html", msg=msg)

# DEFAULT ROUTE
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("login.html")

# Run the app
app.run(host="0.0.0.0", port=8080)




