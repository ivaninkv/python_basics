def input_data():
    return [input() for _ in range(3)]


def main():
    s, a, b = input_data()

    found = False
    found_iter = 0
    if a not in s:
        found = True

    if not found and a != b:
        for i in range(1000):
            s_new = s.replace(a, b)
            if s == s_new:
                found = True
                found_iter = i
                break
            s = s_new

    print(found_iter if found else 'Impossible')


if __name__ == "__main__":
    main()
