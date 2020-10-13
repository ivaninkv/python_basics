import artsy
import requests
import json


def main():
    token = artsy.get_token()

    # создаем заголовок, содержащий наш токен
    headers = {"X-Xapp-Token": token}
    # инициируем запрос с заголовком
    r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

    # разбираем ответ сервера
    j = json.loads(r.text)

    print(j)


if __name__ == "__main__":
    main()
