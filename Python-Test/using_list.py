#!/usr/bin/python
#FileName:using_list.py

#This is my shopping list 
shop_list = ['apple', 'mango', 'carrot', 'banana']
print 'I need',len(shop_list),'items to buy.'

print 'These items are:',
for item in shop_list:
	print item,
	
print 'I also must buy rice!'
shop_list.append('rice')
print 'OK,I should buy these items now:',shop_list
shop_list.sort()
print 'After sorted,I should buy these:',shop_list
print 'What items I first to buy is:',shop_list[0]
olditem = shop_list[0]
del shop_list[0]
print 'Then i should buy:',shop_list

