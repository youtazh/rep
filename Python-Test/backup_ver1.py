# coding:utf-8
#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time
# 使用os和time模块

# 1. The files and directories to be backed up are specified in a list.
source = ['/home/swaroop/byte', '/home/swaroop/bin']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that
# source列表中指定需要备份的文件和目录

# 2. The backup must be stored in a main backup directory
target_dir = '/mnt/e/backup/' # Remember to change this to what you will be using
# target_dir变量指定,目标目录是我们想要存储备份文件的地方

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
# time.strftime()函数获得zip归档的名称:目前的日期和时间,.zip扩展名,将被保存在 target_dir目录中

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
# zip_command字符串,它包含我们将要执行的命令,join()把source列表转换为字符串

# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED' 
# 使用os.system函数 运行 命令,如果命令成功运行,它返回0,否则它返回错误号

