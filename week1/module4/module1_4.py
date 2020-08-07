from queue import Queue


def input_data():
    n = int(input())
    q = Queue()
    for _ in range(n):
        q.put(input().split())
    return q


def process_data(q, nss, vrs):
    while not q.empty():
        command, ns, vp = q.get_nowait()
        if command == 'create':
            create_ns(ns, vp, nss)
        elif command == 'add':
            add_var(ns, vp, nss, vrs)
        elif command == 'get':
            print(get_var(ns, vp, nss, vrs))


def create_ns(ns, parent, nss):
    nss[ns] = parent


def add_var(ns, var, nss, vrs):
    s = vrs.get(ns, set())
    s.add(var)
    vrs[ns] = s


def get_var(ns, var, nss, vrs):
    while ns is not None:
        s = vrs.get(ns)
        if s is not None and var in s:
            break
        else:
            ns = nss.get(ns)
    return ns


def main():
    q = input_data()
    nss = {'global': None}
    vrs = {}
    process_data(q, nss, vrs)
    # print(nss)
    # print(vrs)


if __name__ == '__main__':
    main()
