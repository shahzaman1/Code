import requests
a = requests.get('https://w3schools.com/python/demopage.htm')
print(a.text)