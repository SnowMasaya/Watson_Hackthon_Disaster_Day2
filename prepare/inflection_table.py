# -*- coding: utf-8 -*-
import utils

"""
* download from
 http://lexsrv3.nlm.nih.gov/LexSysGroup/Projects/lexicon/current/web/release/index.html
"""

INFLECTION_TABLE_URL = "http://lexsrv3.nlm.nih.gov/LexSysGroup/Projects/lexicon/2014/release/LEX/MISC/inflection.table"
ADDRESS_TXT = "inflection.table.txt"


def main(url=INFLECTION_TABLE_URL):
    path = utils.DATASET_HOME + ADDRESS_TXT
    utils.download(url, path)

if __name__ == "__main__":
    main()
