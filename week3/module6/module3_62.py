import artsy
import requests
import json


def read_ids(filename='dataset.txt'):
    authors_ids = []
    with open(filename) as f:
        for line in f:
            authors_ids.append(line.strip())
    return authors_ids


def artsy_request(author_id, token):
    headers = {'X-Xapp-Token': token}
    r = requests.get(f'https://api.artsy.net/api/artists/{author_id}',
                     headers=headers)
    return json.loads(r.text)


def write_result(author_names, filename='authors.txt'):
    with open(filename, 'w', encoding='UTF-8') as f:
        f.writelines('\n'.join(author_names))
        f.write('\n')


def main():
    authors_ids = read_ids()
    token = artsy.get_token()
    author_names = []
    for author_id in authors_ids:
        j = artsy_request(author_id, token)
        author_names.append((j['sortable_name'], int(j['birthday'])))
    author_names.sort()  # сортировака по именам
    author_names.sort(key=lambda x: x[1])  # сортировка по году рождения
    write_result([author[0] for author in author_names])


if __name__ == '__main__':
    main()
