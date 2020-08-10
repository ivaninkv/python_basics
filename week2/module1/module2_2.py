def input_data():
    exp_dict = {}
    req_lst = []
    for _ in range(int(input())):
        data = input().split(' : ')
        exp_dict[data[0].strip()] = set(
            data[1].split()) if len(data) > 1 else None
        if len(data) > 1:
            for elem in data[1].split():
                exp_dict[elem] = exp_dict.get(elem)

    for _ in range(int(input())):
        req_lst.append(input().strip())

    return exp_dict, req_lst


def get_parents(exp_dict, execption):
    parents = exp_dict.get(execption)
    if parents:
        for elem in parents:
            prns = get_parents(exp_dict, elem)
            if prns:
                parents = parents | prns

    return parents


def is_intersect(set1, set2):
    intersect = False
    if set1 and set2:
        intersect = len(set1 & set2) > 0

    return intersect


def main():
    exp_dict, req_lst = input_data()
    # print(get_parents(exp_dict, 'KeyError'))
    wrong_exeption = []
    for i in range(len(req_lst)):
        if i > 0:
            if is_intersect(set(req_lst[:i]),
                            get_parents(exp_dict, req_lst[i])):
                if req_lst[i] not in wrong_exeption:
                    wrong_exeption.append(req_lst[i])

    # print(wrong_exeption)
    for elem in wrong_exeption:
        print(elem)


if __name__ == "__main__":
    main()
