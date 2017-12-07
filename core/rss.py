# coding: utf8

import datetime

import PyRSS2Gen
import requests
from bs4 import BeautifulSoup

from share import const


class RssCrawler(object):

    def __init__(self):
        self.rss = PyRSS2Gen.RSS2(
            title="Ruan YiFeng's Blog",
            link='http://www.ruanyifeng.com',
            description='阮一峰的网络日志',
            lastBuildDate=datetime.datetime.now(),
            pubDate=datetime.datetime.now(),
            items=list()
        )

    def request_html(self, url):
        """
        :param url:
        :return:
        """
        r = requests.get(url, headers={'User-Agent': const.USER_AGENT})
        return r.text

    def generate_rss_item(self, url):
        """
        :param url:
        :return:
        """
        html = self.request_html(url)
        soup = BeautifulSoup(html)
        home_page = soup.find('div', {'id': 'homepage'})
        print(home_page)
