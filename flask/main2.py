
from flask import Flask, render_template, request
import urllib.request
import json
app = Flask(__name__)
api = "0f1f3e23fbbcc5c9b4c24d38e2f08a84"
url = "http://api.openweathermap.org/data/2.5/weather"

app = Flask(__name__)


# Replace with your OpenWeatherMap API key
API_KEY = ""


# Home route to display the form
@app.route("/")
def home():
    return render_template("index2.html")


# Route to fetch and display weather details
@app.route("/get_weather", methods=["POST"])
def get_weather():
    city = request.form.get("city")


    # Validate the input city name
    if not city or not validate_city_name(city):
        return render_template("index2.html", error="Please enter a valid city name!")


    # API Request to OpenWeatherMap
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # For temperature in Celsius
    }
    response = request.get(base_url, params=params)


    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "description": data["weather"][0]["description"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
        }
        return render_template("index2.html", weather=weather)
    elif response.status_code == 404:
        return render_template("index2.html", error="City not found! Please check the name.")
    else:
        return render_template("index2.html", error="Unable to fetch weather data at the moment. Please try again later.")


# Function to validate the city name
def validate_city_name(city):
    """
    Validates the city name input.
    Allows alphabetic characters and spaces.
    """
    return all(part.isalpha() for part in city.split()) and len(city) > 1


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)


























