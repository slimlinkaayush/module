import requests
information=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
print(information.status_code)
import json
data=information.json()
print(type(data))
print(data["quoteText"])
