



# try:
#     f = open('D:/video/1.txt','r')
#
#     print(f.read())
# finally:
#     if f:
#         f.close()
#
with open('D:/video/1.txt','r', encoding='gbk',errors='ignore') as f:
    print(f.read())



# b = open('D:/video/222.jpg','rb')
# print(b.read())
# b.close()

with open('D:/video/1.txt','w',errors='ignore') as f:
    print(f.write("hello world"))