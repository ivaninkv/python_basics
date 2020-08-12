import itertools


def primes():
    def is_prime(n):
        d = n - 1
        while d > 1:
            if n % d == 0:
                return False
            d -= 1
        return True

    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield(n)


def main():
    print(list(itertools.takewhile(lambda x: x <= 31, primes())))


if __name__ == "__main__":
    main()
