#Python 日期和时间
#https://www.runoob.com/python/python-date-time.html

import time
ticks = time.time()
print("current timestamp: ", ticks)

print("============================")
import time

localtime = time.localtime(time.time())
print("本地时间是：", localtime)
print(localtime[2])

print("============================")
localtime = time.asctime( time.localtime(time.time()) )
print( "本地时间为 :", localtime)
print(time.localtime())

print("============================")
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
strptime = time.strptime(a, "%a %b %d %H:%M:%S %Y")
print(strptime)
print (time.mktime(strptime))


print("============================")
# 时间戳转化成元组
yz = time.localtime(0)
print(yz)

# 元组转化成格式化时间字符串
fmts = time.strftime("%Y-%m-%d %H:%M:%S", yz)
print(fmts)

# 元组转化成试驾戳
print(time.mktime(yz))

# 格式化时间字符串专程元组
yz1 = time.strptime(fmts, "%Y-%m-%d %H:%M:%S")
print(yz1)

print("============================")
import calendar

month = calendar.month(2016, 1)
print("以下输出2016年1月份的日历：")
print(month)

print("============================")
print(time.perf_counter())
time.sleep(1)
print(time.perf_counter())

print(time.timezone)
print(time.tzname)

