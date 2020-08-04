def uniq_elem(lst):
    return len(set(map(id, lst)))


def main():
    objects = [1, 2, 1, 2, 3, [1], [1]]
    print(uniq_elem(objects))


if __name__ == "__main__":
    main()
