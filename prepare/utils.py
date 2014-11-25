# -*- coding: utf-8 -*-
import urllib.request
from ftplib import FTP
import socket
import zipfile
import os

DATASET_HOME = "../dataset/"


def download(url, filename):
    with urllib.request.urlopen(url) as response, open(filename, "wb") as f:
        data = response.read()
        f.write(data)

"""
def ftp_download(url, filename):
    site = FTP(url)
    path = os.path.dirname(filename)
    fname = os.path.basename(filename)
    site.login(user=user, passwd=passwd)
    if path:
        site.cwd(path)

    flist = site.mlsd(fname)
    site.quit()
"""


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
    with open(filename, "wb") as outfile:
        for row in rows:
            line = (separator.join(row) + "\n").encode("utf-8")
            outfile.write(line)
