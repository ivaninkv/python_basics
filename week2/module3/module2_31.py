class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций
        # (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return pos >= 1

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.pos, self.neg = 0, 0

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in self.iterable:
            self.pos, self.neg = 0, 0
            for f in self.funcs:
                if f(i):
                    self.pos += 1
                else:
                    self.neg += 1
            if self.judge(self.pos, self.neg):
                yield i


def main():
    mf = multifilter([i for i in range(31)], lambda x: x % 2 == 0,
                     lambda x: x % 3 == 0, lambda x: x % 5 == 0,
                     judge=multifilter.judge_half)
    print(list(mf))


if __name__ == "__main__":
    main()
