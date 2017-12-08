# coding: utf8

import datetime

import PyRSS2Gen
import requests
from bs4 import BeautifulSoup

from share import const


class RssCollection(object):
    url = 'http://www.ruanyifeng.com/blog'

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
        headers = {
            'user-agent': const.USER_AGENT,
            'referer': const.REFER_URL
        }
        r = requests.get(url, headers=headers)
        if r.encoding != 'utf8':
            r.encoding = 'utf8'
        return r.text

    def generate_rss_item(self, url):
        """
        :param url:
        :return:
        """
        print('fetch: %s' % url)
        html = self.request_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('title').text
        div = soup.find('div', {'class': 'entry-location'})
        if not div:
            soup.decompose()
            self.url = None
            return None
        self.url = div.find('a')['href']
        soup.decompose()
        rss_item = PyRSS2Gen.RSSItem(
            title=title,
            link=url,
            description=title,
            pubDate=datetime.datetime.now()
        )
        return rss_item

    def generate_rss(self):
        """
        :return:
        """
        html = self.request_html(self.url)
        soup = BeautifulSoup(html, 'html.parser')
        self.url = soup.find('div', {'id': 'entry-1967'}).find('a')['href']
        soup.decompose()
        while self.url:
            rss_item = self.generate_rss_item(self.url)
            self.rss.items.append(rss_item)

    def write_xml(self):
        """
        :return:
        """
        with open('atom.xml', 'w') as f:
            self.rss.write_xml(f, 'utf8')
