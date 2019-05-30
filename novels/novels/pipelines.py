# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import codecs,json

class NovelsPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(host="localhost",user="root",password="123456", db="novels")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        print(item)
        sql = "insert into bk_book_name(name, type_id, author, desp) select %s, %s, %s, %s from dual where not exists (select name from bk_book_name where name=%s and author=%s)"
        args = (item["book_name"], 1, item['author'], item["desp"], item["book_name"], item['author'])
        self.cursor.execute(sql, args)
        self.conn.commit()
        self.cursor.execute("select id from bk_book_name where name=%s and author=%s", (item["book_name"], item['author']))
        book_id = self.cursor.fetchone()[0]
        sql2 = "insert into bk_book_content(name, content, book_id, num) values(%s, %s, %s, %s)"
        args2 = (item["name"], item["content"], book_id, item['num'])
        self.cursor.execute(sql2, args2)
        self.conn.commit()
        return item
    
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


class JsonWithEncodingPipeline(object):
    #自定义json文件的导出
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding="utf-8")
    def process_item(self, item, spider):
        #将item转换为dict，然后生成json对象，false避免中文出错
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item
    #当spider关闭的时候
    def spider_closed(self, spider):
        self.file.close()



# import MySQLdb.cursors
# from twisted.enterprise import adbapi

# #连接池ConnectionPool
# #    def __init__(self, dbapiName, *connargs, **connkw):
# class MysqlTwistedPipline(object):
#     def __init__(self, dbpool):
#         self.dbpool = dbpool

#     @classmethod
#     def from_settings(cls, settings):
#         dbparms = dict(
#             host = settings["MYSQL_HOST"],
#             db = settings["MYSQL_DBNAME"],
#             user = settings["MYSQL_USER"],
#             passwd = settings["MYSQL_PASSWORD"],
#             charset='utf8',
#             cursorclass=MySQLdb.cursors.DictCursor,
#             use_unicode=True,
#         )
#         #**dbparms-->("MySQLdb",host=settings['MYSQL_HOST']
#         dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)

#         return cls(dbpool)

#     def process_item(self, item, spider):
#         #使用twisted将mysql插入变成异步执行
#         query = self.dbpool.runInteraction(self.do_insert, item)
#         query.addErrback(self.handle_error, item, spider) #处理异常

#     def handle_error(self, failure, item, spider):
#         #处理异步插入的异常
#         print (failure)

#     def do_insert(self, cursor, item):
#         #执行具体的插入
#         #根据不同的item 构建不同的sql语句并插入到mysql中
#         insert_sql, params = item.get_insert_sql()
#         cursor.execute(insert_sql, params)
