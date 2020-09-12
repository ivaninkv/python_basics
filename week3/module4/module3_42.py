import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re


def main():
    # url = input()
    # res = requests.get(url)
    # if res.ok:
    #     result = []
    #     soup = BeautifulSoup(res.text, 'lxml')
    #     links_with_text = [a['href'] for a in soup.find_all('a', href=True) if a.text]
    #     for link in links_with_text:
    #         parsed_uri = urlparse(link)
    #         print(parsed_uri)
    #         site = parsed_uri.hostname if parsed_uri.hostname else parsed_uri.path
    #         if site not in result:
    #             result.append(site)
    #     result.sort()
    #     for url in result:
    #         print(url)

    # inp = '''
    # <a href="http://stepic.org/courses">
    # <a href='https://stepic.org'>
    # <a href='http://neerc.ifmo.ru:1345'>
    # <a href="ftp://mail.ru/distib" >
    # <a href="ya.ru">
    # <a href="www.ya.ru">
    # <a href="../skip_relative_links">
    # '''

    url = input()
    res = requests.get(url)
    if res.ok:
        match = re.findall('''(a.+href=['\"])(\w+://)?(\w+[\w.-]+)''', res.text)
        sites = sorted(list(set([x[2] for x in match])))
        for site in sites:
            print(site)


if __name__ == "__main__":
    main()
