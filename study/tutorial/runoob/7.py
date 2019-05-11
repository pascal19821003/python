#Python 列表(List)
#https://www.runoob.com/python/python-lists.html

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

print("============================")
#list = []          ## 空列表
#list.append('Google')   ## 使用 append() 添加元素
#list.append('Runoob')
#print (list)

print("============================")
list1 = ['physics', 'chemistry', 1997, 2000]
print (list1)
del list1[2]
print ("After deleting value at index 2 : ")
print (list1)

print("============================")
L=["Google", "Runoob", 'Taobao']
print(L[2])
print(L[-2])
print(L[1:])

print("============================")
print(len([1, 2, 3]))
print([1, 2, 3] + [4, 5, 6])
print(['Hi!'] * 4)
print(3 in [1, 2, 3])
for x in [1,2,3]: print (x)

print("===============list=============")

aTuple=( 'xyz', 'zara', 'abc')
aList=list(aTuple)

print("列表元素：", aList)

print("============================")
aList=[123, 'xyz', 123, 'zara','abc']
aList.append(2009)
print("Updated List: ", aList)
print("count of 123: ", aList.count(123))
print(aList.index('zara'))
aList.insert(3, "hhh")
print(aList)
aList.pop(-1)
print(aList)
aList.reverse()
print(aList)
