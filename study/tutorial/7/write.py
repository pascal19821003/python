f=open("aa","w")
f.write('this is a test\n')

value = ("the answer", 42)
s=str(value)
f.write(s)

tell = f.tell()
print(f"{tell}")
f.closed