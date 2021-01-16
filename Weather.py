''''''
import pyowm
import Location
owm = pyowm.OWM('3c4ed4e7dddd46ba019f3cabc40ad041')
# Get location (remind me to edit so automatically find location)
def getObs():
  loc = Location.get_city()+', '+Location.get_code()
  return loc
# Printing Data
def display(temp,press,humid,description):
  print('\n===================================')
  print('\nTemperature : '+str(temp)+'\N{DEGREE SIGN}')
  print('\nWind Speed : '+str(press))
  print('\nHumidity : '+str(humid))
  print('\nDescription : '+description)  

def getWeather():
  town = getObs()
  obs = owm.weather_at_place(town)
  weather = obs.get_weather()
  temp = weather.get_temperature('celsius')['temp']
  detail = weather.get_detailed_status()
  wind = weather.get_wind()['speed']
  humidity = weather.get_humidity()
  display(temp,wind,humidity,detail)
  resp = 'The temperature in '+Location.get_city()+' is '+str(temp)+' degrees, with a wind speed of '+str(wind)+', and humidity of '+str(humidity)+'. which indicates that it is '+detail
  return str(resp)

def monWeather(loc):
  obs = owm.weather_at_place(loc)
  weather = obs.get_weather()
  temp = weather.get_temperature('celsius')['temp']
  detail = weather.get_detailed_status()
  wind = weather.get_wind()['speed']
  humidity = weather.get_humidity()
  display(temp,wind,humidity,detail)
  resp = 'The temperature in '+loc+' is '+str(temp)+' degrees, with a wind speed of '+str(wind)+', and humidity of '+str(humidity)+'. which indicates that it is '+detail
  return str(resp)
    

 



