l = ['michael','sarah','tracy','bob','jcke']
# 取list或tuple的部分元素
# 可以用循环 但是十分繁琐
# python提供了切片（slice）操作符
print(l[0:3])
# 从0开始 不包括3    0 1 2三个元素
print(l[:3])
# if start from zero,it can be omitted(省略）
print(l[-2:])
# slice from the bottom(倒数切片)

l1 = list(range(100))
print(l1[:10:2])
# the first 10 number,one for every two.
print(l1[::5])
# all numbers,one for every 5

tuple1 = (0,1,2,3,4,5)
#tuple can not be modified(修改)

s = 'abcdefg'
print(s[:3])
#string is list also

l2 = 'hello'
print(l2[9:10])
