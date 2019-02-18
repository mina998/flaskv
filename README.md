# 第三版 Scrapy 改写
1. 加入开机运行 python3 /root/AmzCrawler/webserver/run.py >> web.log
2. 加入定时任务 25 1 * * * cd /root/AmzCrawler/crawler/ && /bin/sh cron.sh (定时抓取)
