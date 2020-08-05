from queue import Queue


def is_relation(clss, parent, child):
    parents = clss[child]
    if parent in clss and child in clss:
        if (parents is not None and parent in parents) or (parent == child):
            return True
        elif parents is not None:
            for elem in parents:
                if is_relation(clss, parent, elem):
                    return True
    return False


def input_data(clss, q):
    for _ in range(int(input())):
        data = input().split(' : ')
        clss[data[0]] = set(data[1].split()) if len(data) > 1 else None
        if len(data) > 1:
            for elem in data[1].split():
                clss[elem] = clss.get(elem)
    for _ in range(int(input())):
        q.put(input().split())


def main():
    clss = {}
    q = Queue()
    input_data(clss, q)
    # print(clss)
    for _ in range(q.qsize()):
        req = q.get_nowait()
        is_rel = is_relation(clss, req[0], req[1])
        print('Yes' if is_rel else 'No')


if __name__ == "__main__":
    main()
