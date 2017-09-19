'''

操作文件和目录
'''
import os

print(os.name)

# print(os.uname())  在windows上不提供


print(os.environ)

print(os.environ.get('PATH'))

print(os.path.abspath('.'))



# f = os.path.join('D:/video/','testdir')
# # os.mkdir(f)
#
# os.rmdir(f)

print(os.path.split('/Users/michael/testdir/file.txt'))


print(os.path.splitext('D:/video/1.txt'))

# os.rename('D:/video/1.py','D:/video/1.txt')

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

