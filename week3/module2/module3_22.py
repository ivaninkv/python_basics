def input_data():
    return [input() for _ in range(2)]


def substr_count(s, t):
    count = 0
    while len(s) > 0 and t in s:
        count += 1
        s = s[s.find(t) + 1 if s.find(t) > 0 else 1:]

    return count


def main():
    s, t = input_data()
    print(substr_count(s, t))


if __name__ == "__main__":
    main()
