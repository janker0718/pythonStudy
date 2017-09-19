'''

python单元测试
'''
import re

'''
文档测试
'''


m = re.search('(?<=abc)def', 'abcdef')

print(m.group(0))

