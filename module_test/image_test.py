'''
    # 操作image
'''

from PIL import Image

im = Image.open('abc.png');
print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')

import  sys
print(sys.path)
# 运行时修改path
sys.path.append('/Users/michael/my_py_scripts')