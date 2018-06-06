import urllib.request

url = r"http://placekitten.com/g/1000/1000"

response = urllib.request.urlopen(url)
cat_img = response.read()

fp = open("cat1.jpg","wb")
fp.write(cat_img)
fp.close()
print("ok")
