import pyowm
owm = pyowm.OWM('74d85d5912f2ce1e765decd654674675')
observation = owm.weather_at_place('Accra,Ghana')
w = observation.get_weather()
 
print(w.get_wind())
print(w.get_humidity())
print(w.get_temperature())

wind = w.get_wind()
print(wind['deg'])
