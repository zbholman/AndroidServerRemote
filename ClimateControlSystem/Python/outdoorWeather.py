import pyowm #Python Library, Open Weather Map

#Register API Key with source
API_key = '89cb9b3c8c3c1ee033be08ffcfd26076'
owm = pyowm.OWM(API_key)

#Register a lcoation: city,state AND print
location = 'Philadelphia,PA'
print('Location:',location)
 
#Find a location to observe outdoor weather
obs = owm.weather_at_place(location)
w = obs.get_weather()

#Check outdoor Fahrenheit temperature and print
outdoorFahrenheit = w.get_temperature('fahrenheit')
print('Fahrenheit:',outdoorFahrenheit['temp'])

#Check outdoor Humidity percentage and print
outdoorHumidity = w.get_humidity()
print('Humidity:',outdoorHumidity,'%')
