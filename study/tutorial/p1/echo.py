def echo(a,b):
    print(a +  " " +  b)

#if __name__ == "__main__":
#    echo('a','d')


from s1 import fibo
fibo.fib(100)

from s1.fibo import fib
fib(100)

