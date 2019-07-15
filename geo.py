from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.reverse("5.560718, -0.1819926")
print(location.address)
print((location.latitude, location.longitude))

location2 = geolocator.reverse("52.5098014, 13.3755897912911")
print(location2.address)
print((location2.latitude, location2.longitude))

distance = ((location.latitude - location2.latitude) , (location2.longitude - location.longitude))
print("")
print("Distance is: " + str(distance))