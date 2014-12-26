# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from toolbox import file_tool as tool


DATASET_HOME = os.path.join(os.path.dirname(__file__), "../dataset/")


def read_file(path):
    return tool.read_file(path)


def write_file(filename, rows, separator="\t"):
    path = DATASET_HOME + filename
    tool.write_file(path, rows, separator)


def unzip(path):
    return tool.unzip(path)


def download(url, path=None):
    return tool.download(url, path)
