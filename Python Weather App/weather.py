# Imports the tkinter library and gives it the name "tk"
# tkinter is used to create the GUI window
import tkinter as tk

# Imports the requests library
# Used to send HTTP requests to the OpenWeatherMap API
import requests


# Imports the time library
# Used for converting sunrise/sunset timestamps into readable times
import time

def getWeather(canvas): # This function runs when the user presses Enter in the text box

    city = textfield.get()     # Gets the city name typed into the input box

    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=ffcaebd982d99a5d9de8dd019a46f228" # Creates the API URL using the city name and API key

    json_data = requests.get(api).json() # Sends a GET request to the API and converts the response into JSON data

    condition = json_data['weather'][0]['main']     # Gets the weather condition (e.g. Clouds, Rain, Clear)

    # Gets the current temperature
    # OpenWeatherMap gives temperature in Kelvin, so we convert it to Celsius   
    temp = int(json_data ['main']['temp'] - 273.15)

    min_temp = int(json_data ['main']['temp_min'] - 273.15)  # Gets the minimum temperature and converts it to Celsius
    max_temp = int(json_data ['main']['temp_max'] - 273.15)   # Gets the maximum temperature and converts it to Celsius

    pressure = json_data['main']['pressure']  # Gets the atmospheric pressure
    humidity = json_data['main']['humidity']  # Gets the humidity percentage
    wind = json_data['wind']['speed'] #Gets wind speed
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))  # Converts sunrise timestamp into a readable time
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))  # Converts sunset timestamp into a readable time


    final_info = condition + "\n" + str(temp) + "°C" # Creates the main weather information text

    # Creates the extra weather details text
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)  # Updates the first label with weather condition and temperature
    label2.config(text = final_data)  # Updates the second label with extra weather details


canvas = tk.Tk() # Creates the main application window
canvas.geometry("600x500") # Sets the window size
canvas.title("Weather App") # Sets the window title

f = ("poppins", 15, "bold") # Font for the detailed weather information
t = ("poppins", 35, "bold") # Larger font for the temperature display

textfield = tk.Entry(canvas, font = t) # Creates a text input box where the user types the city

textfield.pack(pady = 20) # Adds the text box to the window with padding

textfield.focus() # Automatically selects the text box when the app starts

textfield.bind('<Return>', getWeather) # Runs getWeather when the user presses Enter

label1 = tk.Label(canvas, font = t) # Creates the main weather display label

label1.pack() # Adds it to the window

label2 = tk.Label(canvas, font = f) # Creates the detailed information label

label2.pack() # Adds information label to the window

canvas.mainloop() # Keeps the window running until the user closes it

