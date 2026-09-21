# Weather API Streamlit

## Project Overview

Weather API Streamlit is a simple web application built using **Python** and **Streamlit** that provides real-time weather information for any city. The application uses the **Open-Meteo Geocoding API** to find the city's coordinates and the **Open-Meteo Forecast API** to retrieve current weather data.

## Project Objective

The objective of this project is to demonstrate how Python applications can integrate with external APIs to display real-time weather information through an interactive Streamlit interface.

## Features

* Search weather by city name
* Displays current temperature
* Displays relative humidity
* Displays wind speed
* Real-time weather data
* Simple and user-friendly interface

## Technologies Used

* Python
* Streamlit
* Requests
* Open-Meteo Geocoding API
* Open-Meteo Forecast API

## Project Structure

```text
Weather-API-Streamlit/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/Weather-API-Streamlit.git
```

### Step 2: Open the project folder

```bash
cd Weather-API-Streamlit
```

### Step 3: Install the required libraries

```bash
pip install -r requirements.txt
```

## Requirements

```text
streamlit
requests
```

## Run the Application

Execute the following command:

```bash
streamlit run app.py
```

The application will open in your default web browser.

## How It Works

1. Enter a city name.
2. The Geocoding API converts the city into latitude and longitude.
3. The Forecast API retrieves the current weather.
4. The application displays temperature, humidity, and wind speed.

## Example

### Input

```text
Chennai
```

### Output

```text
Temperature : 31°C
Humidity    : 72%
Wind Speed  : 14 km/h
```

## API Used

### Open-Meteo Geocoding API

Converts a city name into geographical coordinates.

### Open-Meteo Forecast API

Retrieves real-time weather information using latitude and longitude.

## Learning Outcomes

* API Integration with Python
* HTTP Requests using Requests
* JSON Data Processing
* Streamlit Web Application Development
* Real-Time Weather Applications

## Future Enhancements

* 7-day weather forecast
* Weather icons and animations
* Multiple city comparison
* Automatic location detection
* Improved UI design

## Conclusion

This project demonstrates how to build a real-time weather application using **Python**, **Streamlit**, and the **Open-Meteo API**. It provides an easy and interactive way to check current weather conditions by simply entering a city name.

## Author

**Keerthiga K U**

B.Sc. Computer Science with Artificial Intelligence

