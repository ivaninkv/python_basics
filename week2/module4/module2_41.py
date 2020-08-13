def main():
    with open('dataset_24465_4.txt') as f:
        lst = f.readlines()

    with open('res1.txt', 'w') as f:
        f.writelines(lst[::-1])


if __name__ == "__main__":
    main()
