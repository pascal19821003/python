#import support
#support.print_func("runnoob")

from package_runoob.runoob1 import rb1
from package_runoob.runoob2 import rb2
import package_runoob.runoob2

rb1()
rb2()

print(dir(package_runoob.runoob2))
print(package_runoob.runoob2.__doc__)
print(package_runoob.runoob2.__file__)
print(package_runoob.runoob2.__loader__)
print(package_runoob.runoob2.__name__)
print(package_runoob.runoob2.__package__)
print("spec",package_runoob.runoob2.__spec__)
print("builtins",package_runoob.runoob2.__builtins__)
print("cached",package_runoob.runoob2.__cached__)
