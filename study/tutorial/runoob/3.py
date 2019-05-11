num = -1
if num == 3:            # 判断num的值
    print ('boss')
elif num == 2:
    print ('user')
elif num == 1:
    print ('worker')
elif num < 0:           # 值小于零时输出
    print ('error')
else:
    print ('roadman')     # 条件均不成立时输出

print("==============================")


num = 111
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print ('hello')
else:
    print ('undefine')

