'''
    tuple(定义之后不能被修改，并且定义的时候元素就要被确定下来)
'''

t = (1,2)
print(t)


print(t.count(2))

age = 20
if age >= 20:
     print("true")
else:
     print("false")

s = input('birth: ')

birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')