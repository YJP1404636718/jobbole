# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import datetime
import re

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class ArticlesspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


#添加语句
def add_jobbole(values):
    return values+"-jobbole"


# 调整时间的格式
def date_convert(value):
    try:
        # 调整获取到的时间，将其规范化
        create_date = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        # 如果异常的话则获取当前的时间
        create_date = datetime.datetime.now().date()
    return create_date


#获得数量
def get_nums(value):
    match_re = re.match(".*?(\d+).*", value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0
    return nums


# 获取标签中的值
def remove_comment_tags(value):
#     去掉tag中的评论
    if "评论" in value:
        return ""
    else:
        return value


# 将值返回去，front_image_url得到的是str，爬虫无法下载，必须转换
def return_value(value):
    return value


class ArticleItemLoader(ItemLoader):
#     自定义ItemLoader
# 获取第一条数据
    default_output_processor = TakeFirst()


class JobBoleArticleItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
#     Field表示任何传递进来的数据都可以接收，字符、字典、元组
#     创建时间
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(",")
    )

    content = scrapy.Field()



