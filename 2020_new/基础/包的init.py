#/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
包的__init__.py  是导入包的时候默认执行的文件
作用：导入的时候会初始化环境和函数
    在这个文件中的函数可以直接通过包名进行调用  ： pack.show
    当  from A import * 时，   __all__: 在模块中如果不定义__all__=['包名', '']就可以访问所有的模块里的包
                                        在包中则相反，只有定义了才可以访问

'''
