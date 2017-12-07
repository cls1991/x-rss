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
        if r.encoding != 'utf8':
            r.encoding = 'utf8'
        return r.text

    def generate_rss_item(self, url):
        """
        :param url:
        :return:
        """
        html = self.request_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('title').text
        soup.decompose()
        rss_item = PyRSS2Gen.RSSItem(
            title=title,
            link=url,
            description=title,
            pubDate=datetime.datetime.now()
        )
        return rss_item

    def generate_rss(self, url):
        """
        :param url:
        :return:
        """
        html = self.request_html(url)
        soup = BeautifulSoup(html, 'html.parser')
        latest_page_url = soup.find('div', {'id': 'entry-1967'}).find('a')['href']
        # @TODO: traversal all pages
        rss_item = self.generate_rss_item(latest_page_url)
        self.rss.items.append(rss_item)

    def write_xml(self):
        """
        :return:
        """
        with open('atom.xml', 'w') as f:
            self.rss.write_xml(f, 'utf8')
