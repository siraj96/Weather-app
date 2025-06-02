import streamlit as st
import requests

# Tomorrow.io API Key
API_KEY = "7Ar3E8YuVaQXjUM5fc9AmgXcjZl7cZTX"

# Weather Code Mapping
weather_codes = {
    1000: "Clear ☀️",
    1001: "Cloudy ☁️",
    1100: "Mostly Clear 🌤️",
    1101: "Partly Cloudy ⛅",
    1102: "Mostly Cloudy 🌥️",
    2000: "Fog 🌫️",
    2100: "Light Fog 🌫️",
    4000: "Drizzle 🌧️",
    4001: "Rain 🌧️",
    4200: "Light Rain 🌦️",
    4201: "Heavy Rain 🌧️",
    5000: "Snow ❄️",
    5100: "Light Snow 🌨️",
    5101: "Heavy Snow ❄️",
    6000: "Freezing Drizzle 🌧️",
    6001: "Freezing Rain 🌧️",
    6200: "Light Freezing Rain 🌧️",
    6201: "Heavy Freezing Rain 🌧️",
    7000: "Ice Pellets 🌨️",
    7101: "Heavy Ice Pellets 🌨️",
    7102: "Light Ice Pellets 🌨️",
    8000: "Thunderstorm ⛈️"
}

# App title
st.set_page_config(page_title="🌦️ Weather App", layout="centered")
st.title("🌦️ Weather App")
st.write("Get current weather and 6-hour forecast using Tomorrow.io")

# Input
city = st.text_input("Enter a city name", value="Delhi")

if st.button("Get Weather"):
    if city:
        url = f"https://api.tomorrow.io/v4/weather/forecast?location={city}&apikey={API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            forecast = data['timelines']['hourly'][0]
            temp = forecast['values']['temperature']
            code = forecast['values']['weatherCode']
            desc = weather_codes.get(code, "Unknown")

            st.subheader(f"🌍 {city.title()}")
            st.write(f"**Current Temp:** {temp}°C")
            st.write(f"**Condition:** {desc}")

            # 6-hour Forecast
            st.markdown("### 🕒 Next 6 Hours Forecast")
            for hour in data['timelines']['hourly'][:6]:
                time = hour['time'][11:16]  # Get HH:MM
                temp = hour['values']['temperature']
                code = hour['values']['weatherCode']
                desc = weather_codes.get(code, "Unknown")
                st.write(f"**{time}** → {temp}°C, {desc}")

        else:
            st.error(f"Failed to get data for {city}.")
    else:
        st.warning("Please enter a city.")
