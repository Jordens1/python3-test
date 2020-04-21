#/usr/bin/env python
# _*_ coding:utf-8 _*_
import logging
'''
使用示例
a = logger()
a.warning("1")

其中还有可以配置日志在文件中输出的，包括日志的切割，多线程中日志的应用。具体参考：
https://cloud.tencent.com/developer/article/1354396
'''

def logger():
    # create logger
    logger = logging.getLogger("xishi")
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger


