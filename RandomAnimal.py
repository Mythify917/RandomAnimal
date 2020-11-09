import requests


def dog_api():
    url = f'https://random.dog/woof.json'
    res = requests.get(url).json()
    return res['url']


dog = dog_api()


def cat_api():
    url = f"http://aws.random.cat/meow"
    res = requests.get(url).json()
    return res['file']


cat = cat_api()


def fox_api():
    url = f"https://randomfox.ca/floof/"
    res = requests.get(url).json()
    return res['image']


fox = fox_api()


def panda_api():
    url = f"https://some-random-api.ml/img/panda"
    res = requests.get(url).json()
    return res['link']


panda = panda_api()


def bird_api():
    url = "https://some-random-api.ml/img/birb"
    res = requests.get(url).json()
    return res['link']


bird = bird_api()


def koala_api():
    url = "https://some-random-api.ml/img/koala"
    res = requests.get(url).json()
    return res['link']


koala = koala_api()
