# coding: utf8

import os

from core import rss

# checkout to project directory
project = os.path.split(os.path.realpath(__file__))[0]
os.chdir(project)


def main():
    """
    :return:
    """
    rs = rss.RssCollection()
    rs.generate_rss()
    rs.write_xml()


if __name__ == '__main__':
    main()
