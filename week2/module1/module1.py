import random


def foo(number=None):
    if not number:
        random.seed()
        number = random.randint(1, 3)
    if number == 1:
        raise ZeroDivisionError
    elif number == 2:
        raise ArithmeticError
    else:
        raise AssertionError


def main(number=None):
    try:
        foo(number)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ArithmeticError:
        print("ArithmeticError")
    except AssertionError:
        print("AssertionError")


if __name__ == "__main__":
    main()
