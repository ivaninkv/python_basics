class Buffer:
    def __init__(self):
        self.lst = []

    def add(self, *a):
        self.lst += a
        self.cnt = len(self.lst) // 5
        if self.cnt > 0:
            for i in range(self.cnt):
                print(sum(self.lst[:5]))
                del self.lst[:5]

    def get_current_part(self):
        return self.lst


def main():
    pass


if __name__ == "__main__":
    main()
