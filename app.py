from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

# WeatherBit API endpoint and API key
api_endpoint = "http://api.weatherbit.io/v2.0/"
api_key = "7993abaeb9a0423f931813215ee14f2a"  # Replace with your actual API key

#Version solo current weather
# Function to get current weather data
def get_current_weather(city):
    url = f"{api_endpoint}current?city={city}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# Route for index page
@app.route("/")
def index():
    city = "La Plata"  # Default city
    current_weather = get_current_weather(city)
    return render_template("index.html", current_weather=current_weather)

# Route for city search
@app.route("/city/<city>")
def city(city):
    current_weather = get_current_weather(city)
    return render_template("index.html", current_weather=current_weather)

if __name__ == "__main__":
    app.run(debug=True)