# Weather app - main point is to learn how to connect to API at AirNow.gov

from tkinter import *
from PIL import ImageTk,Image
# Need to import requests to get the data from the website and json to read it.
import requests
import json


# Create a tkinter instance root is customary but can name it anything.
root = Tk()
    
# Put a caption or title on our window
root.title("Message Boxes")
root.iconphoto(False, PhotoImage(file='TD.png'))
    
# Set the size of the window
root.geometry("450x200")

# URL from API at Airnow.gov 5 mile radius
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=80521&distance=5&API_KEY=30A683FB-283D-4D7B-A223-0AD334EEEBA9

# URL from API at Airnow.gov 1 mile radius
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=80521&distance=1&API_KEY=30A683FB-283D-4D7B-A223-0AD334EEEBA9
# This uses requests to get the json file from airnow.gov and puts the json object into api_request


try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=80521&distance=1&API_KEY=30A683FB-283D-4D7B-A223-0AD334EEEBA9")

    # this parses the json object into api. It returns a python list containing 3 dictionaries.
    # API's tend to be different so you just have to look at the output to figure out what you're being given.
    api = json.loads(api_request.content)
    
    # Build text for our label
    city = api[0]['ReportingArea']
    # print(city)
    qualityo3 = api[0]['AQI']
    categoryo3 = api[0]['Category']['Name'] 
    combinedo3 = f"O3 Air Quality: {qualityo3}-{categoryo3}"
    # Now set the color
    if categoryo3 == 'Good':
        o3bg = '#0C0'
    elif categoryo3 == 'Moderate':
        o3bg = '#FFFF00'
    elif categoryo3 == 'Unhealthy for Sensitive Groups':
        o3bg = '#FF9900'
    elif categoryo3 == 'Unhealthy':
        o3bg = '#FF0000'
    elif categoryo3 == 'Very Unhealthy':
        o3bg = '#990066'
    elif categoryo3 == 'Hazardous':
        o3bg = '#660000'
    root.configure(background=o3bg)

    qualitypm25 = api[1]['AQI']
    categorypm25 = api[1]['Category']['Name'] 
    combinedpm25 = f"PM2.5 Air Quality: {qualitypm25}-{categorypm25}"
    
    # Now set the color
    if categorypm25 == 'Good':
        pm25bg = '#0C0'
    elif categorypm25 == 'Moderate':
        pm25bg = '#FFFF00'
    elif categorypm25 == 'Unhealthy for Sensitive Groups':
        pm25bg = '#FF9900'
    elif categorypm25 == 'Unhealthy':
        pm25bg = '#FF0000'
    elif categorypm25 == 'Very Unhealthy':
        pm25bg = '#990066'
    elif categorypm25 == 'Hazardous':
        pm25bg = '#660000'

    qualitypm10 = api[2]['AQI']
    categorypm10 = api[2]['Category']['Name'] 
    combinedpm10 = f"PM10 Air Quality: {qualitypm10}-{categorypm10}"

    # Now set the color
    if categorypm10 == 'Good':
        pm10bg = '#0C0'
    elif categorypm25 == 'Moderate':
        pm10bg = '#FFFF00'
    elif categorypm25 == 'Unhealthy for Sensitive Groups':
        pm10bg = '#FF9900'
    elif categorypm25 == 'Unhealthy':
        pm10bg = '#FF0000'
    elif categorypm25 == 'Very Unhealthy':
        pm10bg = '#990066'
    elif categorypm25 == 'Hazardous':
        pm10bg = '#660000'

except Exception as e:
    # api = "Error..."
    print (api)
# We're going to want ReportingArea, AQI, and Category (Category is a dictonary inside a distionary)

cityLabel = Label(root, text="Location: " + city, font=("Helvetica", 20), bg=o3bg )
# cityLabel.pack(pady=10)
cityLabel.grid(row=0,column=0, pady=10, padx=10, sticky=W)
o3Label = Label(root, text=combinedo3, font=("Helvetica", 20), bg=o3bg)
# o3Label.pack(pady=10)
o3Label.grid(row=1,column=0, pady=10, padx=10, sticky=W)
pm25Label = Label(root, text=combinedpm25, font=("Helvetica", 20), bg=pm25bg)
# pm25Label.pack(pady=10)
pm25Label.grid(row=2,column=0, pady=10, padx=10, sticky=W)
pm10Label = Label(root, text=combinedpm10, font=("Helvetica", 20), bg=pm10bg)
# pm10Label.pack(pady=10)
pm10Label.grid(row=3,column=0, pady=10, padx=10, sticky=W)

# And the main event loop
root.mainloop()

