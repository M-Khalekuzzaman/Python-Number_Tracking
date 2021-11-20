'''
import phonenumbers
from phonenumbers import timezone,geocoder,carrier
from opencage.geocoder import OpenCageGeocode
phoneNumbers = phonenumbers.parse("+601124112588")
timeZone = timezone.time_zones_for_number(phoneNumbers)
Carrier = carrier.name_for_number(phoneNumbers,'en')
Region = geocoder.description_for_number(phoneNumbers,'en')
Key = '5fbba725bba044b6acae76c343f549d5'
Geocoder = OpenCageGeocode(Key)
query = str(Region)
results = geocoder.geocode(query)
# print(results)
print(phoneNumbers)
print(timeZone)
print(Carrier)
print(Region)
'''



# phone number country name
import phonenumbers
import folium
from my_number import number
from phonenumbers import geocoder
Key = '5fbba725bba044b6acae76c343f549d5'
sanNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(sanNumber,'en')
print(yourLocation)

# service provider name
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,'en'))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location = [lat,lng])
folium.Marker([lat,lng],popup = yourLocation ).add_to((myMap))

# save map in html file
myMap.save("myLocation.html")

