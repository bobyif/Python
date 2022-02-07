import phonenumbers
import folium
from TheNumber import number
from phonenumbers import geocoder
Key = "c92893f688284738991dae6471b817a6"
samNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)

## get service provider
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(yourLocation)
result = geocoder.geocode(query)

lat = result[0]["geometry"]["lat"]
lng = result[0]["geometry"]["lng"]

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng], popup = yourLocation).add_to(myMap)

myMap.save("Location.html")