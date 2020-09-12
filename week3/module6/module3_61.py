import requests


def input_data():
    res = []
    while True:
        try:
            inp = input()
            if inp == '':
                break
            else:
                res.append(inp)
        except EOFError:
            break

    return res


def get_number_info(num):
    url = f'http://numbersapi.com/{num}/math?json=true'
    res = requests.get(url)
    return res.json()['found']


def main():
    numbers = input_data()
    res = ['Interesting' if get_number_info(x) else 'Boring' for x in numbers]

    with open('res.txt', 'w') as f:
        f.write('\n'.join(res) + '\n')


if __name__ == "__main__":
    main()
