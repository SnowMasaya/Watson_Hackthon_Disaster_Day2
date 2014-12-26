# -*- coding: utf-8 -*-
import sys
import os
from collections import Counter
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
from toolbox import file_tool


def make_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def read_file():
    lines = []
    path = make_path("../dataset/address.txt")
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line.replace("\n", "") for line in lines]

    return lines


def main(head=5, tail=5):
    # knock1: count lines of file
    lines = read_file()
    print("knock1: line count is {0}".format(len(lines)))

    # knock2: replace tab to space
    replaced = [ln.replace("\t", " ") for ln in lines]

    # knock3: split column and save these to file
    splitted = [ln.split(" ") for ln in replaced]
    col1 = [ln[0] for ln in splitted]
    col2 = [ln[1] for ln in splitted]
    file_tool.write_file(make_path("cat1.txt"), col1)
    file_tool.write_file(make_path("cat2.txt"), col2)

    # knock4: reconstruct file from splited files(in knock3)
    col1_re = file_tool.read_file(make_path("cat1.txt"))
    col2_re = file_tool.read_file(make_path("cat2.txt"))

    def trim_cr(line_with_cr):
        return line_with_cr.replace("\n", "")

    restructured = ["\t".join(list(map(trim_cr, columns))) for columns in zip(col1_re, col2_re)]
    file_tool.write_file(make_path("re_address.txt"), restructured)
    knock4_validate = True
    if len(lines) == len(restructured):
        for index, line in enumerate(lines):
            if lines[index] != restructured[index]:
                knock4_validate = False
                break
    else:
        knock4_validate = False

    if not knock4_validate:
        raise Exception("knock4 is failed! check knock1 to 4.")
    else:
        print("knock 2 to 4 seems good!")

    # knock5: show head x lines
    print("knock5. show head {0} lines.".format(head))
    for line in replaced[:head]:
        print(line)

    # knock6: show tail x lines
    print("knock6. show tail {0} lines.".format(tail))
    for line in replaced[-tail:]:
        print(line)

    # knock7: count kinds of column1
    def count_kinds(array):
        kinds = Counter()
        for item in array:
            kinds[item] += 1
        return kinds

    col1_kinds = count_kinds(col1)
    print("knock7. show counted result of top 10.")
    print(col1_kinds.most_common(10))  # show top 10

    # knock8: sort by column2
    sorted_by_col2 = sorted(splitted, key=lambda cols: cols[1])
    print("knock8. show sorted result of top {0}.".format(head))
    for columns in sorted_by_col2[:head]:
        print(" ".join(columns))

    # knock9: sort by column2 and column1
    sorted_by_col2_col1 = sorted(splitted, key=lambda cols: cols[1] + cols[0])
    print("knock9. show sorted result of top {0}.".format(head))
    for columns in sorted_by_col2_col1[:head]:
        print(" ".join(columns))

    # knock10:  count kinds of column2
    col2_kinds = count_kinds([trim_cr(x) for x in col2_re])  # use file in knock3
    print("knock10. show counted result of top 10.")
    print(col2_kinds.most_common(10))  # show top 10


if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(int(sys.argv[1]), int(sys.argv[2]))
    else:
        main()

