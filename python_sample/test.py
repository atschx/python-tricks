#!/usr/bin/env python
#coding:utf-8
#author:albert
#date:2015-09-14

import logging


global_logger = None

def  init_logger():

	#声明全局的logger
	global global_logger

	if global_logger:
		return global_logger

	global_logger = logging.getLogger("sample")

	#config
	global_logger.setLevel(logging.DEBUG)

	# 创建一个handler，用于写入日志文件
	fh = logging.FileHandler('/tmp/sample-debug.log')
	fh.setLevel(logging.DEBUG)

	# 再创建一个handler，用于输出到控制台
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)

	# 定义handler的输出格式
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	ch.setFormatter(formatter)

	# 给logger添加handler
	global_logger.addHandler(fh)
	global_logger.addHandler(ch)
	return global_logger

def  main():
	init_logger()
	global_logger.debug("123123")
	logger = init_logger()
	logger.debug("test")

	from storage.redis.connection import get_redis_connection
	redis = get_redis_connection()
	for x in xrange(1,10000):
		redis.set("albert%s" % x,"test%s" % x)
		pass
	

if __name__ == '__main__':
	main()