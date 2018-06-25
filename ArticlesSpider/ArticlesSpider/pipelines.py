# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
import codecs

from scrapy.pipelines.images import ImagesPipeline
from twisted.enterprise import adbapi



class ArticlesspiderPipeline(object):
    def process_item(self, item, spider):
        return item


#对数据库操作异步话操作
class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool=dbpool
    @classmethod
    # 从settings取数据 ，cls指的是class
    def from_settings(cls, settings):
        dbparms=dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        # adbapi.ConnectionPool构造器，进行数据库的异步操作语句
        dbpool=adbapi.ConnectionPool("MySQLdb", **dbparms)
        # 返回取得的值
        return cls(dbpool)

    # #使用twistd异步插入
    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error)

    # #处理异步插入的异常
    def handle_error(self, failure):
        print(failure)
    #     #执行具体的插入

    def do_insert(self, cursor,item):
        insert_sql="""
                           insert into jobbole_article(url_object_id,title, url, fav_nums, create_date,tags, praise_nums, comment_nums, front_image_url)

                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                       """

        cursor.execute(insert_sql,
                       (item["url_object_id"], item["title"], item["url"], item["fav_nums"], item["create_date"]
                        , item["tags"], item["praise_nums"], item["comment_nums"], item["front_image_url"]))


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if "front_image_path" in item:
            for ok, value in results:
                image_file_path = value["path"]
            item["front_image_path"] = image_file_path
        return item
