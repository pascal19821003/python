https://www.techbeamers.com/

https://www.runoob.com/python/python-numbers.html

https://www.tutorialspoint.com/python3/python_lists.htm



=================================error=================
1. TypeError: 'list' object is not callable

https://www.cnblogs.com/cnhkzyy/p/8833720.html

由于变量list和函数list重名了，所以函数在使用list函数时，发现list是一个定义好的列表，而列表是不能被调用的，因此抛出一个类型错误


2. NameError: name 'tup' is not defined
   产生原因： 
    del tup
    print(tup) 
    
3. KeyError: 'Alice'
    产生原因：
        print "dict['Alice']: ", dict['Alice']
        其中dict中并没有key为Alice的键值对。
      
4.  TypeError: 'type' object is not subscriptable        
    产生原因：
    del dict
    print(dict['Age'])
    
5. TypeError: printme() missing 1 required positional argument: 'str'
    产生原因：
    调用函数时，没有传递参数
    
6.    