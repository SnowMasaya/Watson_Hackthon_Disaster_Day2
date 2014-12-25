import os
import zipfile
import requests


def read_file(path):
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    return lines


def write_file(path, rows, separator="\t"):
    with open(path, "wb") as outfile:
        for row in rows:
            line = ""
            if isinstance(row, list) or isinstance(row, tuple):
                line = separator.join(row) + "\n"
            else:
                line = row + "\n"
            outfile.write(line.encode("utf-8"))


def unzip(path):
    files = []
    d = os.path.dirname(path) + "/"

    with zipfile.ZipFile(path, "r") as zdir:
        for zf in zdir.namelist():
            if os.path.basename(zf):
                f_path = d + str(zf)
                files.append(f_path)
                with open(f_path, "wb") as unziped:
                    unziped.write(zdir.read(zf))

    return files


def download(url, path=None):
    content = None
    r = requests.get(url)
    if path:
        with open(path, "wb") as f:
            f.write(r.content)
    else:
        content = r.text

    return content
