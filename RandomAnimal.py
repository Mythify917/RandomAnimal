import requests


def dog():
    """
    Uses the API to get a random image of a dog.
    """
    url = f'https://random.dog/woof.json'
    res = requests.get(url).json()
    return res['url']


def cat():
    """
    Uses the API to get a random image of a cat.
    """
    url = f"http://aws.random.cat/meow"
    res = requests.get(url).json()
    return res['file']


def fox():
    """
    Uses the API to get a random image of a fox.
    """
    url = f"https://randomfox.ca/floof/"
    res = requests.get(url).json()
    return res['image']
