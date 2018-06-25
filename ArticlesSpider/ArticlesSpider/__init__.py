# -*- coding: utf-8 -*-
from urllib import parse

import scrapy
from scrapy.http import Request

from ArticlesSpider.items import JobBoleArticleItem


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']