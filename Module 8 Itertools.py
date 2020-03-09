Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from itertools import*
>>> for i in chain([1,2,3], ['a', 'b', 'c']):
	print i
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i)?
>>> print(i)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(i)
NameError: name 'i' is not defined
>>> $ python intertools_izip.py
SyntaxError: invalid syntax
>>> (1, 'a')
(1, 'a')
>>> (2, 'b')
(2, 'b')
>>> (3, 'c')
(3, 'c')
>>> 