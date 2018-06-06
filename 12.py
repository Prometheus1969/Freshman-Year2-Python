
import urllib.request

response = urllib.request.urlopen('http://placekitten.com/g/500/500')
cat_img = response.read()

with open("cat_5--_600.jpg","wb") as f:
    f.write(cat_img)
