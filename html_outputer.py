#!/usr/bin/python
#coding:utf8
########################################################################################################
# File Name: html_outputer.py
# Author: luohong
# mail:luohong213@163.com
# Create Time: 2016年03月27日 星期日 13时26分29秒
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return

        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table")
        fout.write("</body>")
        fout.write("</html>")
