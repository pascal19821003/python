#Python 异常处理
#https://www.runoob.com/python/python-exceptions.html

try:
    fh=open("testfile","w")
    fh.write("这是一个测试文件，用于测试异常!!")
except:
    print("Error: 没有找到文件或读取文件失败")
else:
    print( "内容写入文件成功")
    fh.close()


print("=============2222===============")
try:
    fh=open("testfile","w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print( "内容写入文件成功")
    fh.close()


print("=============3333===============")
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except:
    print("Error: 没有找到文件或读取文件失败")
finally:
    print("必须执行")
    # fh.close()


print("=============4444===============")
try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print ("关闭文件")
        fh.close()
except Exception as v:
    print ("Error: 没有找到文件或读取文件失败", v)



print("=============5555===============")
# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except Exception as v:
        print ("参数没有包含数字\n", v)
# 调用函数
temp_convert("xyz");


print("=============6666===============")
# 定义函数

def functionName( level ):
    if level <1:
        raise Exception(level,"qipa")
        # The code below to this would not be executed
        # if we raise the exception
    return level

try:
    l = functionName(-10)
    print ("level = ",l)
except Exception as e:
    print ("error in level argument",e)