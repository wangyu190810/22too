
### centos ImportError: No module named _sqlite3

	Traceback (most recent call last):
	  File "test.py", line 1, in <module>
	    import db
	  File "/data/hkstock/stis/run/log/process/db.py", line 2, in <module>
	    import sqlite3
	  File "/usr/local/lib/python2.7/sqlite3/__init__.py", line 24, in <module>
	    from dbapi2 import *
	  File "/usr/local/lib/python2.7/sqlite3/dbapi2.py", line 28, in <module>
	    from _sqlite3 import *
	ImportError: No module named _sqlite3

出现的原因是没有_sqlite3这个内部库，但是使用find 命令查找之后发现：
	
	find / -name _sqlite3.so
	/usr/usr/lib/python2.6/lib-dynload/_sqlite3.so
	/usr/local/service/python2.7/lib/python2.7/lib-dynload/_sqlite3.so
	/usr/lib64/python2.6/lib-dynload/_sqlite3.so
	
然后将：
	
	cp /usr/local/service/python2.7/lib/python2.7/lib-dynload/_sqlite3.so /usr/local/lib/python2.7/sqlite3/
	
问题解决，这个问题用了四个小时，原因是因为，我第一次操作是这样的：

	cp /usr/usr/lib/python2.6/lib-dynload/_sqlite3.so /usr/local/lib/python2.7/sqlite3/
	
然后出现奇怪的bug，

1. 不能使用sqlalchemy进行操作。
2. 字符显示不全，

第一个问题，解决方法直接替换掉sqlalchemy，使用原生sqlite3执行
但是第二个问题，无法解决，最终发现[stackoverflow](http://stackoverflow.com/questions/11394013/problems-with-python-2-7-3-on-centos-with-sqlite3-module/34432084#34432084)
这个问题是自己使用的问题，没有使用find ，而是直接将2.6 下的copy过去。

