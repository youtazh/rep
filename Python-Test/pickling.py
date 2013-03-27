#coding:utf-8
#!/usr/bin/python
# Filename: pickling.py

import cPickle as p
#import pickle as p

shoplistfile = 'shoplist.data'
# the name of the file where we will store the object

shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = file(shoplistfile, 'w')
p.dump(shoplist, f) # dump the object to a file
# 调用储存器模块的dump函数，把对象储存到打开的文件中。这个过程称为 储存 。
f.close()

del shoplist # remove the shoplist

# Read back from the storage
f = file(shoplistfile)
storedlist = p.load(f)
# 调用模块的load函数的返回来取回对象。这个过程称为 取储存 。
print storedlist 