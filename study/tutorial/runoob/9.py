#Python 字典(Dictionary)
#https://www.runoob.com/python/python-dictionary.html

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

#print ("dict['Alice']: ", dict['Alice'])

print("=========================")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict["Age"]=8
dict["School"]="RUNOOB"
print(dict)

print("=========================")
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict["Name"]
print(dict)
dict.clear()
print(dict)
del dict
#print(dict['Age'])
print(type(dict))

print("=========================")
dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = dict1.copy()
print ("New Dictionary : %s" %  str(dict2))