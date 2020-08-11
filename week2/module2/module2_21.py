import datetime


def input_data():
    d = []
    d += map(int, input().split())
    d = datetime.date(d[0], d[1], d[2])

    days = int(input())

    return d, days


def main():
    d, days = input_data()

    td = datetime.timedelta(days=days)
    d += td
    print(d.year, d.month, d.day)


if __name__ == "__main__":
    main()
