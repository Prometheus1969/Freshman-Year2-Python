#list.py

import random
list1 = list(range(10))
#建立数字列表
print(list1)
list2 = ["Jerry", "Jack111", "Peter"]
#建立字符串列表
print(list2)
list3 = list1
print(list3)
list4 = [ x for x in list2 ]
#利用遍历建立列表
print(list4)
list5 = [1, 2, 3, "a", "b", "c"]
if 10 in list5 :
    print("10存在于list5中")
if "d" in list5 :
    print("d存在于list5中")
#判断列表中的存在
list6 = list5 * 2
#列表元素×2
print(list6)
print(list5[3])
print(type(list5[3]))
list5 = list5 + ["d", "e" ,"f"]
#列表的连接
print(list5)
random.shuffle(list1)
#列表的乱序
print(list1)
print(max(list1))
print(min(list1))
print(len(list1))
#得到列表的最大值，最小值，和长度
list1 = list(range(10, 21 ,1))
list1.append(33)
#列表后追加新元素
print(list1)
list1.extend([44, 55, 66])
#列表后追加新列表
print(list1)
list1.reverse()
#列表逆序
print(list1)
list1.sort()
#列表排序，从小到大
print(list1)
list1.reverse()
print(list1)
list1[0:4] = ['a', 'b']
#列表部分替换
print(list1)
