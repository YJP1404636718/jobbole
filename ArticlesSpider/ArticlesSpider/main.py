# -*- coding: utf-8 -*-
import os
import sys
from scrapy.cmdline import execute
# os.path.abspath(__file__)  获取当前文件的文件目录
# os.path.dirname  获取当前文件夹的父目录


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 类似于语句 scrapy crawl jobbole 执行爬虫
execute(["scrapy", "crawl", "jobbole"])