#数值
var1 = 1
print(var1)

del var1
var1 = 2
print(var1)

print(type(var1))

var2 = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
var2 +=1
print(var2)
print(type(var2))

var3 = 0.1
var4 = 10e2
print(type(var3))
print(var4)
print(type(var4))

var5 = int(var4)
print(var5)
print(type(var5))



import math
print(dir(math))
print(math.ceil(4.3))
print(math.floor(10.2))
print(math.log(100, 10))
print(math.sqrt(4))

print(math.pi)
print(math.e)
print(math)


import random
print(random.choice(range(10)))
print(random.random())
l = ['a', 'b', 1, 3]
print(l)

random.shuffle(l)
print(l)