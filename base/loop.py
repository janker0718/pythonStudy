'''
    Python中的循环
'''

names= ['jack','mary']
for name in names:
    print(name)
numbers = [0,1,2,3,4,5]
sum  = 0
for x in numbers:
    sum = sum + x
print(sum)
sum2 = 0
for x in range(10):
    sum2 = sum2 + x
print(sum2)
sum3 = 0
n = 99
while n>0 :
    sum3 = sum3 + n
    n = n-3
print(sum3)