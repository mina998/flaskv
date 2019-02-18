from scrapy import Item, Field

class TaobaoItem(Item):
    # define the fields for your item here like:

    id   = Field()

    asin = Field()
    # 获取产品价格
    price = Field()
    # 获取产品库存
    stock = Field()
    # 获取BSR排名
    bsr = Field()
    # 产品图片
    img = Field()




