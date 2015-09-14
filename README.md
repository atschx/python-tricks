# python-tricks

> Life is short,use python!

## 源码**头文件**

``` python
#!/usr/bin/env python
# coding:utf-8
```

还有这种：

``` python
#!/usr/bin/python
# -*- coding:utf8 -*-
```

第一句引导出python环境变量，`-*- coding:utf8 -*—`是为了兼容emacs。[查看详情](https://www.python.org/dev/peps/pep-0263/)

## 记录日志

> 日志logging使用示例

``` python
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
```

## 存储(cassandra)

创建名为`sample`的keyspaces.

``` 
CREATE KEYSPACE IF NOT EXISTS sample WITH replication ={'class':'SimpleStrategy','replication_factor':2}
```

[详情参考这里](http://datastax.github.io/python-driver/api/index.html)

## 后记

python框架和应用的区别？

如果一个框架帮你自定义了存储模型机策略它是半成品还是成品(Stream-Framwork)