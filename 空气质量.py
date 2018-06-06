#空气质量.py

pm = eval(input("请输入pm值："))
if 0<pm<35 :
    print("优,可以户外运动")
elif 35<=pm<75 :
    print("良,适度运动")
else :
    print("污染,不建议户外运动")
