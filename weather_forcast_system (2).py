
import streamlit as st
import requests

# Function to fetch weather data from OpenWeatherMap
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

# App title
st.title("🌤️ Simple Weather App")

# Text input for city name
city = st.text_input("Enter city name:")

# If a city is entered, get weather info
if city:
    api_key = "your_api_key_here"  # 🔑 Replace with your actual OpenWeatherMap API key
    data = get_weather(city, api_key)

    # If city found, show data
    if data.get("cod") == 200:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        st.write(f"**Temperature:** {temp} °C")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Description:** {desc.capitalize()}")
    else:
        st.error("City not found ❌")
