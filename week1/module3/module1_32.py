def C(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return C(n - 1, k) + C(n - 1, k - 1)


def input_data():
    return map(int, input().split())


def main():
    n, k = input_data
    print(C(n, k))


if __name__ == "__main__":
    main()
