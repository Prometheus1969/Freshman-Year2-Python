
fp = open("data.txt","r")
s1= []
s2 = []
for k in fp:
    s1.append(int(k))
fp.close()
s1.sort()
for i in s1:
    s2.append(str(i)+"\n")
fp = open("data2.txt","w")
fp.writelines(s2)
fp.close()
print("完事")
