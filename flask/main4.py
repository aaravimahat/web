from flask import Flask,render_template,request, jsonify
import requests


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index3.html")

@app.route("/locate", methods=["POST"])

def locate():
    district=request.form.get("district", "")

    if not district:
        return jsonify({"error": "district is required"}),400
    
    try:
        url = f"https://nominatim.openstreetmap.org/search?city={district}&format=json&addressdetails=1"
        response=requests.get(url, headers={"User-Agent":"Mozilla/5.0"})
        data=response.json()

        if not data:
            return jsonify({"error":"district not found"}),404
        
        result=data[0]

        address=result.get("address", {})
        state=address.get("state", "Unknown")
        country=address.get("country", "Unknown")

        return jsonify({"state":state, "country":country})
    
    except Exception as e:
        return jsonify({"error":f"an error has occured:{str(e)}"}),500
    
if __name__=="__main__":
    app.run(debug=True)

    

    

        



