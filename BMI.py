#BMI.py
height,weight = eval(input("请输入身高（m）和体重（kg），用空格隔开："))
BMI = weight / pow( height,2 )
if ( BMI < 18.5 ) :
    dom = "偏瘦"
elif ( BMI < 24 ) :
    dom = "正常"
elif ( BMI < 28 ) :
    dom = "偏胖"
else :
    dom = "肥胖"
print("根据我国标准，您的体重 {}".format(dom))
