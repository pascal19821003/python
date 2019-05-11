with open("output.py") as f:

    read = f.read()
    print(read)



f.closed


#
f=open("output.py")
print("##################3")
for line in f:
    print(line)

f.close()


#
f=open("output.py")
print("##################4")
l = list(f)
print(l)

f.close()
