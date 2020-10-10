while True:
    ax = int(input('投射向量的x值'))
    ay = int(input('投射向量的y值'))
    bx = int(input('被投射向量的x值'))
    by = int(input('被投射向量的y值'))
    constant = (ax*bx+ay*by)/(bx**2+by**2)
    print('projection是(',bx*constant,',',by*constant,')')
