#键-值（key-value）储存 dict（dictionary）
d = {'michael':95,'michael':75,'tracy':85}
print(d['michael'])
#无论表有多大查找，速度都不会变慢
d['adam'] = 67
print(d['adam'])
#通过key计算位置哈希算法（hash） key必须是不可变对象
