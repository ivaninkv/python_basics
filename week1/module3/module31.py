def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        return x + (5 - x % 5)


def main():
    print(closest_mod_5(11))


if __name__ == "__main__":
    main()
