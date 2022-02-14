# I want to add the zip code lookup to his stuff and for places that have less than 3 readings,
# loop through the list of dictionaries and show just the ones that exist.
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

quality = ["","",""]
category = ["","",""]
combined = ["","",""]
aqtype = ["","",""]
aqLabel = ["","",""]

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=80521&distance=15&API_KEY=30A683FB-283D-4D7B-A223-0AD334EEEBA9")

    # this parses the json object into api. It returns a python list containing 3 dictionaries.
    # API's tend to be different so you just have to look at the output to figure out what you're being given.
    api = json.loads(api_request.content)
    print(api)
    
    if len(api) == 0:
        combined[0] = "No data within 5 miles of zipcode"
        aqLabel[0] = Label(root, text=combined[0], font=("Helvetica", 20), bg="red")
            # o3Label.pack(pady=10)
        aqLabel[0].grid(row=1,column=0, pady=10, padx=10, sticky=W)

    else:
        # Build text for our label
        city = api[0]['ReportingArea']
        # print(city)
        # print(api[0]['AQI'], type(api[0]['AQI']))
        for num in range(len(api)):
            quality[num] = (str(api[num]['AQI'])) 
            # print(quality[0])
            category[num] = (api[num]['Category']['Name']) 
            # print(category[0])
            aqtype[num] = (api[num]['ParameterName']) 
            # print(aqtype[0])
            combined[num] = f"{aqtype[num]} Air Quality: {quality[num]}-{category[num]}"
            # Now set the color
            if category[num] == 'Good':
                aqbg = '#0C0'
            elif category[num] == 'Moderate':
                aqbg = '#FFFF00'
            elif category[num] == 'Unhealthy for Sensitive Groups':
                aqbg = '#FF9900'
            elif category[num] == 'Unhealthy':
                aqbg = '#FF0000'
            elif category[num] == 'Very Unhealthy':
                aqbg = '#990066'
            elif category[num] == 'Hazardous':
                aqbg = '#660000'
            root.configure(background=aqbg)

            cityLabel = Label(root, text="Location: " + city, font=("Helvetica", 20), bg=aqbg )
            # cityLabel.pack(pady=10)
            cityLabel.grid(row=0,column=0, pady=10, padx=10, sticky=W)
            aqLabel[num] = Label(root, text=combined[num], font=("Helvetica", 20), bg=aqbg)
            # o3Label.pack(pady=10)
            aqLabel[num].grid(row=num+1,column=0, pady=10, padx=10, sticky=W)

        
except Exception as e:
    # api = "Error..."
    print ("ERROR ERROR ERROR " + api)
# We're going to want ReportingArea, AQI, and Category (Category is a dictonary inside a distionary)

# And the main event loop
root.mainloop()

