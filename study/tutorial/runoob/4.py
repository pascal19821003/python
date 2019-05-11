count = 0
while (count<9):
    print("the count is :" , count)
    count = count+1

print("goodbye")


print("================================================ ")
i = 1
while i<10:
    i+=1
    if i%2 > 0 :
        continue
    print(i)

print("================================================ ")
i=1
while 1:
    print(i)
    i += 1
    if i>10:
        break

print("================================================ ")
#import sys
#print(sys.platform)

var = 1
#while var == 1:
   # num = input("Enter a number: ")
    #print("You entered:" , num)

print("Good bye!")


print("================================================ ")
count=0
while count<5:
    print(count , " is less than 5")
    count += 1
else :
    print (count, " is not less than 5")


print("================================================ ")
for letter in "Python":
    print ("current letter is " , letter)

fruits=["banana", "apple", "mango"]
for fruit in fruits:
    print("current fruit is:", fruit)
print("Good bye!")

for index in range(len(fruits)):
    print("当前水果是：", fruits[index])


print("================================================ ")
for num in range( 10 , 20 ) :
    for i in range( 2 , num ) :
        if num%i ==0:
            j = num/i
            print("%d = %d * v %d" %(num, i, j))
            break
    else:
        print (num, "是一个质数")

print("================================================ ")

for letter in "Python" :
    if letter == "h" :
        break
    print("当前字母是： ", letter)

print("================================================ ")

for letter in "Python" :
    if letter == "h" :
        continue
    print("当前字母是： ", letter)


print("================================================ ")
for letter in 'Python':
    if letter == 'h':
        pass
        print ('这是 pass 块')
    print ('当前字母 :', letter)








