# -*- coding: utf-8 -*-
from prepare import utils

"""
* download from
 http://ja.wikipedia.org/wiki/%E7%89%B9%E5%88%A5:%E9%95%B7%E3%81%84%E3%83%9A%E3%83%BC%E3%82%B8
"""

JAPANESE_URL = "http://ja.wikipedia.org/wiki/%E3%82%B4%E3%83%AB%E3%82%B413%E3%81%AE%E3%82%A8%E3%83%94%E3%82%BD%E3%83%BC%E3%83%89%E4%B8%80%E8%A6%A7"
JAPANESE_TXT = "japanese.txt"


def main(url=JAPANESE_URL):
    path = utils.DATASET_HOME + JAPANESE_TXT
    utils.download(url, path)

if __name__ == "__main__":
    main()
