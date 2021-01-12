import requests

print("Requests version: " + requests.__version__)
print("Google status code: " + str(requests.get("http://www.google.com/").status_code))