for i  in range(5) :
    print(i)


print("step=======================")
a = range(0,10,3)
for i in a:
    print(i)

print("negative number")
for i in range(-10, -100, -30) :
    print(i)


print("iterate over the indices of a sequence")
a=['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(list(range(5)))