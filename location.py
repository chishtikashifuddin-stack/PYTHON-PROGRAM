import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder 
from phonenumbers import carrier 

number=input("Enter the phone number with country code :")
phonenumber=phonenumbers.parse(number)
timezone = timezone.time_zones_for_number(phonenumber)
print("timezone:"+str(timezone))
geolocation = geocoder.description_for_number(phonenumber,"en")
print("location:"+geolocation)
service = carrier.name_for_number(phonenumber,"en")
print("service provider :"+service)