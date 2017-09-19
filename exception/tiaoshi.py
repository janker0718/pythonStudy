'''
# 调试
'''

import logging
import pdb

logging.basicConfig(level=logging.INFO)
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10/n


# main()

s = '0'
n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)

def foo1(s):
    n = int(s)
    assert n !=0 , 'n is zero!'
    return 10/n

# foo1('0')
s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10/n)




