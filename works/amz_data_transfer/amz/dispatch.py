import sys
sys.path.append('..')

from amz.amazon import GetProductInfo
from amz.models import Listing, Marks
from amz.sqlite import session
from configure import LOGS_PATH
import time


def run():

    while True:

        exem = session.query(Listing)

        listing = exem.filter(Listing.status == 0).first()

        # 是否查询完成
        if listing == None:

            session.query(Listing).filter(Listing.status == 1).update({'status':'0'})

            session.commit()

            break

        # 当天未查询完成的
        tA = time.localtime(time.time())

        # 当前时间大于1点10分10秒就退出并导出未抓取ASIN
        if tA.tm_hour + tA.tm_min + tA.tm_sec < 1 + 10 + 10:

            listing = session.query(Listing.asin).filter(Listing.status == 0).all()

            if listing == None: break

            nowdate = time.strftime('%Y-%m-%d %H:%M:%S', tA)

            listing = ', '.join([asin[0] for asin in listing])

            content = '[%s] %s \n' % (nowdate, listing)

            path = LOGS_PATH+'/other.txt'

            with open(path, 'a+', encoding='utf-8') as fb:

                fb.write(content)

            break

        info = GetProductInfo(listing.asin, seller=listing.seller).get()

        if not info: continue

        data = {"status": "1", "img": info['img']} if not listing.img else {"status": "1"}

        exem.filter(Listing.asin == listing.asin).update(data)

        mark = Marks(asin_id=listing.id,bsr=info['bsr'],stock=info['stock'],price=info['price'])

        session.add(mark)

        session.commit()

        time.sleep(20)


if __name__ =='__main__':

    run()