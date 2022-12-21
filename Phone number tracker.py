import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
phone_number_1 = phonenumbers.parse("+91123456789","CH")
result = geocoder.description_for_number(phone_number_1,"en")
print(result)
if result=="India":
    phone_number_1 = phonenumbers.parse("+91123456789","RO")
    print(carrier.name_for_number(phone_number_1,"en"))

