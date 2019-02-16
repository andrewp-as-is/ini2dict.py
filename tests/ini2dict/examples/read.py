#!/usr/bin/env python
import ini2dict
import os

path = os.path.join(os.path.dirname(__file__),"file.ini")
data = ini2dict.read(path)
print(data)
