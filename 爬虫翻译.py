import urllib.request
import json
import urllib.parse

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

data = {}

data["doctype"] = "json"

p = input("\n请输入要翻译的话：")

data["i"] = p

data = urllib.parse.urlencode(data).encode("utf-8")

res = urllib.request.urlopen(url, data)

html = res.read().decode("utf-8")

target = json.loads(html)

print("\n翻译中...\n")
print("翻译结果:\n")
print(target["translateResult"][0][0]["tgt"])
print("\n")
