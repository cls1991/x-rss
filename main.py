# coding: utf8

import os

# 切换工作目录到项目根目录
project = os.path.split(os.path.realpath(__file__))[0]
os.chdir(project)

from core import rss


def main():
    """
    :return:
    """
    rs = rss.RssCrawler()
    rs.generate_rss('http://www.ruanyifeng.com/blog')
    rs.write_xml()


if __name__ == '__main__':
    main()
