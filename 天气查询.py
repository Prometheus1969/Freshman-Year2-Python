import urllib.request
import json
import pickle

city_file = open('city.pkl','rb')
city = pickle.load(city_file)
city_file.close()

city_name = input('请输入城市:')
city_no = city[city_name]

#查询全天的url：http://www.weather.com.cn/data/cityinfo/101010100.html
url = "http://www.weather.com.cn/data/cityinfo/" + city_no + ".html"

#实时http://www.weather.com.cn/data/sk/101010100.html

request_info =urllib.request.urlopen(url)#打开url

#读入打开的url
html = request_info.read().decode('utf-8')
jsonDatas = json.loads(html)


#打印信息
city        = jsonDatas["weatherinfo"]["city"]
temp1       = jsonDatas["weatherinfo"]["temp1"]
temp2       = jsonDatas["weatherinfo"]["temp2"]
weather     = jsonDatas["weatherinfo"]["weather"]
ptime       = jsonDatas["weatherinfo"]["ptime"]

content_allday = city + "全天天气:" + weather + "\n"+ "最高气温:" + temp1+ "\n" + "最低气温:"  + temp2 + "\n"+ "发布时间:" + ptime

print(content_allday)

#查询实时天气
url = "http://www.weather.com.cn/data/sk/" + city_no + ".html"
#实时http://www.weather.com.cn/data/sk/101010100.html

request_info =urllib.request.urlopen(url)#打开url

#读入打开的url
html = request_info.read().decode('utf-8')
jsonDatas = json.loads(html)

#打印信息
city        = jsonDatas["weatherinfo"]["city"]
temp        = jsonDatas["weatherinfo"]["temp"]
fx          = jsonDatas["weatherinfo"]["WD"]        #风向
fl          = jsonDatas["weatherinfo"]["WS"]        #风力
sd          = jsonDatas["weatherinfo"]["SD"]        #相对湿度
tm          = jsonDatas["weatherinfo"]["time"]

content_realtime = "\n" + city + "实时天气:" + " " + temp + "℃ " + fx + fl + " " + "相对湿度" + sd + " "  + "发布时间:" + tm
print(content_realtime)
