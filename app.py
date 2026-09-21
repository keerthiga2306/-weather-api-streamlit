import streamlit as st
import requests

st.set_page_config(
    page_title="Weather API",
    page_icon="☁️"
)

st.title("Weather API")
st.write("Get current weather information for any city.")

city = st.text_input("Enter City Name", placeholder="Example: Chennai")

if st.button("Get Weather"):

    if city.strip() == "":
        st.warning("Please enter a city name.")

    else:
        # Geocoding API
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params
        )

        geo_data = geo_response.json()

        if "results" not in geo_data:
            st.error("City not found. Please enter a valid city.")

        else:
            location = geo_data["results"][0]

            latitude = location["latitude"]
            longitude = location["longitude"]

            # Weather API
            weather_url = "https://api.open-meteo.com/v1/forecast"

            weather_params = {
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
                "timezone": "auto"
            }

            weather_response = requests.get(
                weather_url,
                params=weather_params
            )

            weather_data = weather_response.json()
            current = weather_data["current"]

            st.success(f"Weather in {location['name']}")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Temperature",
                    f"{current['temperature_2m']} °C"
                )

            with col2:
                st.metric(
                    "Humidity",
                    f"{current['relative_humidity_2m']}%"
                )

            with col3:
                st.metric(
                    "Wind Speed",
                    f"{current['wind_speed_10m']} km/h"
                )

            st.write(
                "Weather Code:",
                current["weather_code"]
            )
