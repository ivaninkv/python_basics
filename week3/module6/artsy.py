import configparser
import requests
import json


CONF_PATH = 'artsy.conf'


def get_token():
    config = configparser.ConfigParser()
    config.read(CONF_PATH)
    try:
        token = config.get('Settings', 'token')
    except configparser.NoOptionError:
        client_id = config.get('Settings', 'client_id')
        client_secret = config.get('Settings', 'client_secret')

        # инициируем запрос на получение токена
        r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                          data={
                            "client_id": client_id,
                            "client_secret": client_secret})

        # разбираем ответ сервера
        j = json.loads(r.text)

        # достаем токен
        token = j["token"]

        # пишем токен
        config.set('Settings', 'token', token)
        with open(CONF_PATH, "w") as f:
            config.write(f)

    return token


if __name__ == "__main__":
    get_token()
