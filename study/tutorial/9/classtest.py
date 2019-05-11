class Complex:
    def __init__(self, realpart, imagepart):
        self.r=realpart
        self.i = imagepart

x = Complex(1,-92.5)
print(x.i)
print(x.r)


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

print(MyClass.i)
print(MyClass.f)

myClass =  MyClass();
print(myClass.f())
