import datetime, sqlite3

class AmazonPipeline(object):

    def __init__(self,sqlite3_db_uri):

        self.sqlite_db_uri = sqlite3_db_uri


    @classmethod
    def from_crawler(cls, crawler):

        return cls(
            sqlite3_db_uri = crawler.settings.get('SQLITE_DB_URI'), # 从 settings.py 提取
        )

    def open_spider(self, spider):

        self.con = sqlite3.connect(self.sqlite_db_uri)

        self.cur = self.con.cursor()


    def close_spider(self, spider):
        self.con.close()

    def process_item(self, item, spider):


        if not item['price'] or not item['stock'] :

            print('ASIN:',item['asin'], '失败! 重新加入查询列队.')

            return item

        item['price'] = str(item['price'][0])
        item['bsr'] = str(item['bsr'][0]).replace(',','')
        item['img'] = item['img'][0]

        row = {
            'bsr':item['bsr'],
            'price':item['price'],
            'stock':item['stock'],
            'asin_id':item['id'],
            'uptime':datetime.datetime.now()
        }

        print('ASIN:', item['asin'], '价格:', item['price'], '库存:', item['stock'])

        insert = "insert into marks (bsr,price,stock,asin_id,uptime) values ('{bsr}','{price}','{stock}','{asin_id}','{uptime}')".format(**row)

        update = 'update listing set status = 1,img = "{img}" where id = {id}'.format(img=item['img'],id=item['id'])
        try:
            self.cur.execute(insert)

            self.cur.execute(update)

            self.con.commit()

        except Exception as e:

            print('Sqlite 语法错误:',e)


        return item
