#coding:utf8
import sys
from fenci import fenci

fc = fenci()
fc.init_fenci()
ret = fc.get_text_fc('王晓明是个大坏蛋，十点二十分天马行空般的去打篮球')
for i in ret:
	print i[0]
	print '-----'