#判断正负数
positive = 0
negative = 0
while 1:
    print("Write down integers")
    integers=int(input())
    if integers>0:
        positive = positive+1
    elif integers<0:
        negative = negative+1
    else:
        pass
    print("there are",positive,'positive and',negative,"negative numbers")