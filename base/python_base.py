'''
Created on 2017年5月25日

@author: zhiyongliu3
'''

'''
print ("please input 3*3 result:")
a = input()
if a == 9 :
    print ("true")
else :
    print ("false")
'''

print ('I\'m \"ok\" ! ')


print (True)
print (3>2)
print (2>3)
print (None)
print (not True)
print (12.3e4)

print(456.789)
# r'''Hello,
print("r\'\'\'Hello,")
# 'Hello, \'Adam\''
print("\'Hello, \\\'Adam\\\'\'")
# r'Hello, "Bart"'
print("r\'Hello, \"Bart\"\'")

print ("包含中文的str")
print(ord('A'))
print(chr(66))

print(chr(25991))

print('\u4e2d\u6587')

str = 'ABC'.encode('ascii')
print(str)
str2 = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

print(str2)

print(len('ABC'))

print(len('中文'.encode('utf-8')))
print('Age: %s. Gender: %s' % (25, True))
r = 'hello'
print('hello' % r)