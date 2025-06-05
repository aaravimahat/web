from flask import Flask, request, render_template
from datetime import datetime
app=Flask(__name__)
@app.route("/")

def a():
    return render_template("index.html")
@app.route("/age", methods=["POST"])

def c():
    try:
        d=int(request.form.get("birth_year"))
        e=datetime.now().year

        if d>e:
            return render_template("index.html", error="Please enter a valid number")
        
        age=e-d
        return render_template("index.html", age=age)
    except ValueError:
        return render_template("index.html",error="Please enter a valid number" )
    
if __name__== "__main__":
    app.run(debug=True)

    

        