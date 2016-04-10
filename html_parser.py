#!/usr/bin/python
#coding:utf8
########################################################################################################
# File Name: html_parser.py
# Author: luohong
# mail:luohong213@163.com
# Create Time: 2016年03月27日 星期日 12时48分28秒
#==============================================================================================
from bs4 import BeautifulSoup
import re
import urlparse
import logging

logging.basicConfig(level=logging.DEBUG,format="[%(asctime)s]%(name)s:%(levelname)s:%(message)s")
class HtmlParser(object):

    def parse(self, page_url, html_content):

        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self.get_new_urls(page_url, soup)
        new_data = self.get_new_data(page_url, soup)
        return new_urls, new_data

    def get_new_urls(self, page_url, soup):
        new_urls = set()
        #/view/123.html
        links = soup.findAll('a', href = re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']
            logging.debug(new_url) 
            new_full_url = urlparse.urljoin(page_url, new_url)
            logging.debug(new_full_url) 
            new_urls.add(new_full_url)
        return new_urls


    def get_new_data(self,page_url,  soup):
        res_data={}

        #url
        res_data['url'] = page_url

        #<dd class="legmmaWgt-lemmaTitle-title"> <h1>python</h1>
        title_node = soup.find('dd', class_ =
                               "lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        #<div class = lemma-summary>
        summary_node = soup.find('div', class_ = 'lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data

