# -*- coding: utf-8 -*-
import csv
from prepare import utils

ZIP_CODE_URL = "http://www.post.japanpost.jp/zipcode/dl/oogaki/zip/ken_all.zip"
ADDRESS_ZIP = "ken_all.zip"
ADDRESS_TXT = "address.txt"


def main(url=ZIP_CODE_URL):
    path = utils.DATASET_HOME + ADDRESS_ZIP
    utils.download(url, path)
    files = utils.unzip(path)
    if len(files) > 0:
        write_address(files[0])
    else:
        print("failed to download or unzip the file. please see at {0}.".format(utils.DATASET_HOME))


def write_address(csvfile):
    PREFECTURE = 6
    CITY = 7
    TOWN = 8

    address_set = set()
    with open(csvfile, newline="") as cf:
        rows = csv.reader(cf, delimiter=",")
        for row in rows:
            address = "".join([row[PREFECTURE], row[CITY]])
            town = row[TOWN]
            if town == "以下に掲載がない場合":
                continue
            else:
                sections = town.split("、")
                for s in sections:
                    house_number_index = s.find("（")
                    if house_number_index > -1:
                        s = s[:house_number_index]
                    address_set.add((address, s))

    dataset = []
    for p, t in address_set:
        dataset.append((p, t))

    utils.write_file(ADDRESS_TXT, dataset)


if __name__ == "__main__":
    main()
