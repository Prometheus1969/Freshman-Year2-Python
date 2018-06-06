#split1.py

fp = open( "dayup.txt ", "r")
xu = []
stu = []
for line in fp :
    (role, speak) = line.split(":", 1)
    if role == "徐老师" :
        xu.append(speak)
    elif role == "同学" :
        stu.append(speak)
fp.close()
fp1 = open("xu.txt", "w")
fp2 = open("stu.txt", "w")
fp1.writelines(xu)
fp2.writelines(stu)
fp1.close()
fp2.close()
    
