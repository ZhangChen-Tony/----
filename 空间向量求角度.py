import math
while 1:
    a1 = int(input('请输入第一个向量的x值'))
    a2 = int(input('请输入第一个向量的y值'))
    a3 = int(input('请输入第一个向量的z值'))
    b1 = int(input('请输入第二个向量的x值'))
    b2 = int(input('请输入第二个向量的y值'))
    b3 = int(input('请输入第二个向量的z值'))
    up = a1*b1+a2*b2+a3*b3
    down1 = a1*a1+a2*a2+a3*a3 
    down2 = b1*b1+b2*b2+b3*b3
    down = down1*down2
    truedown = down**0.5
    mixed = up/truedown
    arc = math.acos(mixed)
    o = math.degrees(arc)
    print('两个向量之间的夹角为',o)
