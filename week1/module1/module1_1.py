def input_data():
    n = int(input())
    lst = [int(input()) for i in range(n)]
    return lst


def sum_lst_element(lst):
    return sum(lst)


def main():
    lst = input_data()
    print(sum_lst_element(lst))


if __name__ == "__main__":
    main()
