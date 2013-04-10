#/usr/bin/python
#coding=utf-8

import _scws


class fenci():
	
	def __init__(self):
		self.xdb_dict_path = ''
		self.txt_dict_path = ''
		self.rule_path = ''
		self.charset = ''
		self.set_xdb_dict()
		self.set_rule()
		self.set_txt_dict()
		self.set_char_set()
		
	def set_xdb_dict(self,path = ''):
		self.xdb_dict_path = path
	
	def set_rule(self,path = ''):
		self.rule_path = path
		
	def set_txt_dict(self,path = ''):
		self.txt_dict_path = path
	
	def set_char_set(self,charset = 'UTF8'):
		self.charset = charset
	
	def init_fenci(self):
		print self.xdb_dict_path
		_scws.scws_new()
		_scws.scws_set_charset(self.charset)
		_scws.scws_set_xdb(self.xdb_dict_path)
		_scws.scws_set_rule(self.rule_path)
		_scws.scws_add_dict(self.txt_dict_path)
		_scws.scws_set_multi(8)
	
	def get_text_fc(self,text):
		ret = _scws.get_res(text)
		return ret
		
	def __del__(self):
		_scws.scws_free()
		
	