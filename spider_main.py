#!/usr/bin/python
# -*- coding: UTF-8 -*-
########################################################################################################
# File Name: spider_main.py
# Author: luohong
# mail:luohong213@163.com
# Create Time: 2016年03月26日 星期六 19时45分17秒
#==============================================================================================

import url_manager, html_outputer, html_downloader,html_parser
import logging
# 设置默认的level为DEBUG# 设置log的格式
logging.basicConfig(level=logging.DEBUG,format="[%(asctime)s]%(name)s:%(levelname)s:%(message)s")
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                logging.info('craw %d : %s' % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break
                count = count + 1
            except Exception as e:
                logging.info("craw failed")
                logging.debug(e)
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
