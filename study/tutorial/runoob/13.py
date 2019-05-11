#Python 文件I/O
#https://www.runoob.com/python/python-files-io.html

#str = input("please input:")
#print("echo:", str)


print("===========================")
fo = open("foo.txt","w")
print("文件名：", fo.name)
print("是否已经关闭：", fo.closed)
print("访问模式：", fo.mode)

#print("末尾是否强制加空格：", fo.softspace)

print("===========================")
fo.write("www.runoob.com!\nVery good site!\n")

fo.close()
print("是否已经关闭：", fo.closed)

print("===========================")
fo=open("foo.txt", "r+")
str= fo.read(10)
print("读取的字符串是：" , str)

position = fo.tell()
print("当前文件位置：", position)

print("================================")
fo.seek(0,0)
position = fo.tell()
print("当前文件位置：", position)

print("================================")
import os
os.rename("foo.txt", "foo2.txt")


print("================================")
os.remove( "foo2.txt")


print("================================")
os.mkdir("test")


print("================================")
#os.rmdir("test")

print("================================")
os.chdir("test")
print(os.getcwd())