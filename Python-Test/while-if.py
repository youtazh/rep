#coding=utf-8
#!/usr/bin/python
# Filename: if.py 
#
number = 23
flag=1
#raw_input函数是一个字符串。通过int把这个字符串转换为整数
while flag:
    guess = int(raw_input('Enter an integer : '))
    if guess == number:
        print 'Congratulations, you guessed it.' # New block starts here
        print "(but you do not win any prizes!)" # New block ends here
        flag = 0
    elif guess < number and guess != 0:
        print 'No, it is a little higher than that' # Another block
    # You can do whatever you want in a block ...

    elif guess > number:
        print 'No, it is a little lower than that' 
    # you must have guess > number to reach here

    else:
        print 'You give up it!'
        flag=0
print 'Done'
# This last statement is always executed, after the if statement is executed 
