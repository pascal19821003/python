#Python 函数
#https://www.runoob.com/python/python-functions.html

def printme(str):
    "print parameters"
    print (str)
    return

printme(str="nihao")

print("============================")
def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print (b) # 结果是 2

print("============================")
def changeme( mylist ):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    #mylist = [1,2,3,4]
    print ("函数内取值: ", mylist)
    return

mylist=[10,20,30]
changeme(mylist)

print("函数外取值：", mylist)

print("============================")
def printinfo( name, age ):
    "打印任何传入的字符串"
    print( "Name: ", name)
    print ("Age ", age)
    return


printinfo(age=50, name="nini")

print("============================")
#可写函数说明
def printinfo( name, age = 35 ):
    "打印任何传入的字符串"
    print ("Name: ", name)
    print ("Age ", age)
    return

printinfo(name="pascal")

print("============================")
def printinfo( arg1, *vartuple ):
    "打印任何传入的参数"
    print ("输出: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return

printinfo(10)
printinfo(10, 1,2,3)

print("============================")
sum=lambda  arg1, arg2:  arg1 + arg2

print(sum(10,20))

print("============================")
def sum(a1, a2):
    " 返回2个参数的和"
    total = a1 + a2
    return  total

total = sum(10,20)
print(total)

print("============================")

total = 0
def sum(a1, a2):
    total = a1 + a2 + b
    print("函数内是局部变量：", total)
    return total

sum (10, 20)
print("函数外是全局变量", total)
