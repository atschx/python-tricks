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

使用logging模块

python框架和应用的区别？

如果一个框架帮你自定义了存储模型机策略它是半成品还是成品(Stream-Framwork)