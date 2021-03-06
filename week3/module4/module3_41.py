import requests
import re


def input_data():
    url_a, url_b = [input() for _ in range(2)]
    return [url_a, url_b]


def get_urls(url):
    finded_urls = []
    res = requests.get(url)
    if res.ok:
        finded_urls.extend(re.findall(r'href=[\'"]?([^\'" >]+)', res.text))
    return finded_urls


def find_intersect(url_a, url_b, max_depth=10, depth=1):
    finded_urls = get_urls(url_a)
    if depth <= max_depth:
        if url_b in finded_urls:
            return True, depth
        for url in finded_urls:
            found, d = find_intersect(url, url_b, max_depth, depth+1)
            if found:
                return True, d

    return False, -1


def main():
    urls = input_data()
    # found, depth = find_intersect(urls[0], urls[1], 2)
    # print('Yes' if found and depth == 2 else 'No')

    # solution for stepik.org
    founded = False
    second_page_urls = []
    first_page_urls = get_urls(urls[0])
    for url in first_page_urls:
        second_page_urls.extend(get_urls(url))
    founded = urls[1] in second_page_urls

    print('Yes' if founded else 'No')


if __name__ == "__main__":
    main()
