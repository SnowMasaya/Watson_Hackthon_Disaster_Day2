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
        write_address(files[0], utils.DATASET_HOME + ADDRESS_TXT)
    else:
        print("failed to download or unzip the file. please see at {0}.".format(utils.DATASET_HOME))


def write_address(address_csv, filename):
    PREFECTURE = 6
    CITY = 7
    TOWN = 8

    address_set = set()
    with open(address_csv, newline="") as csvfile:
        rows = csv.reader(csvfile, delimiter=",")
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

    utils.write_file(filename, dataset)


if __name__ == "__main__":
    main("http://www.post.japanpost.jp/zipcode/dl/oogaki/zip/del_1410.zip")
