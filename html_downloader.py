#!/usr/bin/python
#coding:utf8
########################################################################################################
# File Name: html_downloader.py
# Author: luohong
# mail:luohong213@163.com
# Create Time: 2016年03月27日 星期日 12时19分32秒
#==============================================================================================
import urllib2

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
