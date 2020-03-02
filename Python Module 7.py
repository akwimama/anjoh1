Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import sys
>>> for line  in sys.stdin:
	data=line.strip().split("\t")
	if len(data)= = 6:
		
SyntaxError: invalid syntax
>>> if len(data)==6:
	date,time,item,cost,payment = data
	print "{0}\t{1}".format(item,cost)
	
SyntaxError: invalid syntax
>>> print "{0}\t{1}".format(item,cost)
SyntaxError: invalid syntax
>>> print {0}\t(1}.format(item,cost)
SyntaxError: invalid syntax
>>> 
================================ RESTART: Shell ================================
>>> from datetime import timedelta
>>> #Add 1 day
>>> from datetime import timedelta
>>> d= timedelta(microseconds=-1)
>>> (d.days,d.seconds,d.microseconds)
(-1, 86399, 999999)
>>> d= timedelta(microseconds=3)
>>> (d.days,d.seconds,d.microseconds)
(0, 0, 3)
>>> from datetime import datetime
>>> #get current date
>>> datetime_object=datetime.now(March2202012:35am)
SyntaxError: invalid syntax
>>> daatetime_object=datetime.now(March220201235am)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    daatetime_object=datetime.now(March220201235am)
NameError: name 'March220201235am' is not defined
>>> datetime_object= datetime.now(03222020)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> datetime_object= datetime.now(3222020)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    datetime_object= datetime.now(3222020)
TypeError: tzinfo argument must be None or of a tzinfo subclass, not type 'int'
>>> datetime_object=datetime.now(tz)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    datetime_object=datetime.now(tz)
NameError: name 'tz' is not defined
>>> print(datetime_object)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(datetime_object)
NameError: name 'datetime_object' is not defined
>>> 