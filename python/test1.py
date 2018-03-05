#!/usr/bin/env python
#_*_coding:utf-8_*_

from uuid import uuid1
import struct
i = 123
print i
print 'Hello World!'
print  uuid1().get_hex()
print u'中国人'
print '======='
a = 65
str = struct.pack('i' , a)
print str
print len(str)
print  repr(str)

