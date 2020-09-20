import json


def input_data():
    return json.loads(input())


def get_graph_from_list(lst):
    graph = {}
    for elem in lst:
        graph[elem['name']] = set(elem['parents'])
    return graph


def get_all_parents(graph, start):
    res = graph[start]
    gres = set()
    for elem in res:
        gres |= get_all_parents(graph, elem)
    return res | gres


def main():
    inp = input_data()
    graph = get_graph_from_list(inp)
    for elem in graph:
        graph[elem] = get_all_parents(graph, elem)

    res = {}
    for elem in graph.keys():
        qty = 1
        for i in graph:
            if elem in graph[i]:
                qty += 1
        res[elem] = qty

    for elem in sorted(res):
        print(f'{elem} : {res[elem]}')


if __name__ == "__main__":
    main()
