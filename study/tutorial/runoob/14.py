#Python File(文件) 方法
#https://www.runoob.com/python/file-methods.html
#http://www.cnblogs.com/allenblogs/archive/2010/09/13/1824842.html

file_obj = open("thefile.txt", "r")
try:
    all_the_text = file_obj.read()
    print(all_the_text)
finally:
    file_obj.close()

print("===========================")
fo = open("thefile.txt", "rb")
try:
    while True:
        chunk = fo.read(2)
        if not chunk:
            break
        print(chunk)
finally:
    fo.close()

print("===========================")
fo = open("thefile.txt", "r")
all_lines = fo.readlines()
for l in all_lines:
    print(l)

print("===========================")
output = open("data", "w")
fo = open("thefile.txt", "r")
all_lines = fo.readlines()
for l in all_lines:
    output.write(l)
output.flush()
fo = open("data")
print(fo.read())


print("===============11============")
output = open("data", "w")
fo = open("thefile.txt", "rb")
all_lines = fo.readlines()
for l in all_lines:
    print(type(l.decode()))
    output.write(l.decode())
output.flush()
fo = open("data")
print(fo.read())


print("==============222222222=============")
fo = open("thefile.txt", "rb")
all_lines = fo.readlines()
print(all_lines)
fo.close()
output = open("data2","wb")
output.writelines(all_lines)
output.close()

r= open("data2", "r")
print(r.readlines())
r.close()

a="abc"
encode = a.encode()
print(encode)
