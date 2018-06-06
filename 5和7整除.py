#100以内能被7整除且不能被5整除的整数。py
for i in range(101) :
    if i%7==0 and i%5!=0 :
        print(i,end=" ")
