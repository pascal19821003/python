#!/usr/bin/python
# -*- coding: UTF-8 -*-
# https://www.runoob.com/python/python-variable-types.html

counter=100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print(counter)
print (miles)
print (name)


print("----------------------------")
a = b = c = 1
print(a)
print(b)
print(c)

print("----------------------------")
a, b, c = 1, 2, "john"
print(a)
print(b)
print(c)

print("----------------------------")
s="abcdef"
print(s[5])
print(s[3:5])
print(s[-1])
print(s[-3:])


print("----------------------------")
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)               # 输出完整列表
print (list[0])            # 输出列表的第一个元素
print (list[1:3] )         # 输出第二个至第三个元素
print ( list[2:]  )         # 输出从第三个开始至列表末尾的所有元素
print (tinylist * 2)       # 输出列表两次
print ( list + tinylist)    # 打印组合的列表


print("----------------------------")
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])
print (dict[2])
print (tinydict)
print (tinydict.keys())
print (tinydict.values())

