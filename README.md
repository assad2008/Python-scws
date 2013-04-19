Simple Chinese Word Segmentation Python package
======================
SCWS:http://www.ftphp.com/scws/<br />

使用

#coding:utf8 <br />
import sys <br />
from fenci import fenci<br />

fc = fenci()<br />
fc.init_fenci()<br />
ret = fc.get_text_fc('王晓明是个大坏蛋，十点二十分天马行空般的去打篮球')<br />
for i in ret:<br />
	print i[0]<br />
	print '-----'<br />

