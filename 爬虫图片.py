#cat.py
import urllib.request

url = "http://placekitten.com/1000/1000"

res = urllib.request.urlopen(url)

img = res.read()

with open("cat.jpg", "wb") as f:
    f.write(img)

print("OK")
