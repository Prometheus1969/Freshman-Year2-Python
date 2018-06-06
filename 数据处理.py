#数据处理.py

fp = open("data.txt", "r")
data = []
for x in fp :
    data.append(int(x))
fp.close()
data.sort()
dataS = []
for str in data :
    dataS.append(str(str)+ "\n")
fp = open("data.asc.txt", "w")
fp.writelines(dataS)
fp.close()
print("over")
