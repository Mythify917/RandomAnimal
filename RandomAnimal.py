import requests


def RandomDog():
    url = f'https://random.dog/woof.json'
    res = requests.get(url).json()
    return res['url']


def RandomCat():
    url = f"http://aws.random.cat/meow"
    res = requests.get(url).json()
    return res['file']
