import requests


def RandomDog():
    """
    Uses the API to get a random image of a dog.
    """
    url = f'https://random.dog/woof.json'
    res = requests.get(url).json()
    return res['url']


def RandomCat():
    """
    Uses the API to get a random image of a cat.
    """
    url = f"http://aws.random.cat/meow"
    res = requests.get(url).json()
    return res['file']
