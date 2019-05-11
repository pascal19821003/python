#Python 元组
#https://www.runoob.com/python/python-tuples.html
tup1=()
print(tup1)

print("===================")
tup1=(50,)
print(tup1)
print(type(tup1))

print("====================")
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

print("====================")
tup1=(12, 24.56)
tup2=('abc', 'xyz')
tup3 = tup1 + tup2
print(tup3)

print("====================")
tup = ('physics', 'chemistry', 1997, 2000)
print(tup)
del tup
print("After deleting tup:")
#print(tup)

print("====================")
if 3 in(1,2,3) :
    print( "in tuple!")
else :
    print("not in tuple!")

print("====================")
tup = 1,2,3
print(tup)
print(type(tup))


print(len(tup))
print(min(tup))

l=[1,2,3,5]
tup = tuple(l)
print(tup)


