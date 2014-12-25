# -*- coding: utf-8 -*-
import toolbox.file_tool as tool

DATASET_HOME = "../dataset/"


def write_file(filename, rows, separator="\t"):
    path = DATASET_HOME + filename
    tool.write_file(path, rows, separator)
