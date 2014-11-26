# -*- coding: utf-8 -*-
import requests
import zipfile
import os

DATASET_HOME = "../dataset/"


def download(url, filename=None):
    content = None
    r = requests.get(url)
    if filename:
        with open(filename, "wb") as f:
            f.write(r.content)
    else:
        content = r.text

    return content


def unzip(filename):
    d = os.path.dirname(filename) + "/"
    files = []
    with zipfile.ZipFile(filename, "r") as zdir:
        for zf in zdir.namelist():
            if os.path.basename(zf):
                path = d + str(zf)
                files.append(path)
                with open(path, "wb") as unziped:
                    unziped.write(zdir.read(zf))

    return files


def write_file(filename, rows, separator="\t"):
    path = DATASET_HOME + filename
    with open(path, "wb") as outfile:
        for row in rows:
            line = ""
            if isinstance(row, list) or isinstance(row, tuple):
                line = separator.join(row) + "\n"
            else:
                line = row + "\n"
            outfile.write(line.encode("utf-8"))
