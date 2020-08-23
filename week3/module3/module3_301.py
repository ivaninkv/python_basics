import re


def input_data():
    lst = []
    while True:
        inp = input()
        if inp:
            lst.append(inp)
        else:
            break

    return lst


def match_elem(lst, template=r'.*cat.*cat.*'):
    res = []
    for elem in lst:
        if re.search(template, elem):
            res.append(elem)

    return res


def main():
    lst = input_data()
    for elem in match_elem(lst):
        print(elem)


if __name__ == "__main__":
    main()


# import re
# import sys

# for line in sys.stdin:
#     line = line.rstrip()
#     if re.match(r'.*cat.*cat.*', line):
#         print(line)
