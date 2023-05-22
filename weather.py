# the impoer request is used because we are requesting for some type of data
import requests

API_KEY = "9bbe03c783f524f042a7c337a4296a1a"
# the url we want to hit
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# a code line used along the base url to specify which data exactly we want
# in this case, which cities we want weateher data from
city = input("Enter name of the city: ")
# this code is connecting the base url, to the api key and finaly to the specific data we want for city
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
# generate a response from the requests imported and request url specifically
response = requests.get(request_url)
# 200 is the standarrd code to mean it was successful
# 400 not successful
# status code is used to check the standard code
if response.status_code == 200:
    data = response.json()
    # from the api key we pick tartgeted information, description, main and temp
    weather = data['weather'][0]['description']
#   round of the temp to celsius
    temperature = round(data['main']['temp'] - 273.15, 2)
    # specify the method in which we want the
    print("weather:", weather)
    print("temperature:",temperature, "celsius")
else:
    print("Error occured")
   