'''
# 调试
'''

import logging
logging.basicConfig(level=logging.INFO)
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10/n
def main():
    foo('0')

# main()

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

