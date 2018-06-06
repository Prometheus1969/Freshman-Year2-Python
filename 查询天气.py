import pickle
import json
import urllib.request

f = open( "citylist.ct", "rb" )
city = pickle.load(f)
cityname = input("请输入城市名称：")
citynum = city[cityname]

url = "http://www.weather.com.cn/data/cityinfo/"+citynum+".html"

web_info = urllib.request.urlopen(url)
html = web_info.read().decode("utf-8")
jsondata = json.loads(html)

city = jsondata["weatherinfo"]["city"]
temp1 = jsondata["weatherinfo"]["temp1"]
temp2 = jsondata["weatherinfo"]["temp2"]
weather = jsondata["weatherinfo"]["weather"]
ptime = jsondata["weatherinfo"]["ptime"]

content_allday = city+ "天气:"+ weather+ "\n"+ "最高气温:"+ temp2+ "\n"+ "最低天气"+ temp1 + "\n"+ "发布时间:"+ ptime
print(content_allday)
