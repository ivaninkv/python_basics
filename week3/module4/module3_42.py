import requests
import re


def main():
    url = input()
    res = requests.get(url)
    if res.ok:
        match = re.findall('''(a.+href=['\"])(\w+://)?(\w+[\w.-]+)''',
                           res.text)
        sites = sorted(list(set([x[2] for x in match])))
        for site in sites:
            print(site)


if __name__ == "__main__":
    main()
