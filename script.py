import requests

print("Requests version: " + requests.__version__)
print("Google status code: " + str(requests.get("http://www.google.com/").status_code))
print("GitHub Python Script:\n")
r = requests.get("https://raw.github.com/fredford/cmput404_lab1/master/script.py")
s = requests.get("https://raw.github.com/fredford/cmput404_lab1/master/README.md")

print(r.text)
print(s.text)
