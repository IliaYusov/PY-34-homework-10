import requests
import tqdm

API_URL = 'https://superheroapi.com/api/'
API_TOKEN = '2619421814940190'


def get_id(name):
    response = requests.get(API_URL + API_TOKEN + '/search/' + name)
    results = response.json()['results']
    for result in results:
        if result['name'] == name:
            return result['id']


def get_int(id_):
    response = requests.get(API_URL + API_TOKEN + '/' + id_ + '/powerstats')
    return response.json()['intelligence']


def main():
    heroes = {
        'Hulk': 0,
        'Captain America': 0,
        'Thanos': 0
    }
    for name in tqdm.tqdm(heroes):
        heroes[name] = int(get_int(get_id(name)))
    print(*[f'{hero}-{heroes[hero]}' for hero in list(sorted(heroes, reverse=True, key=heroes.__getitem__))], sep='\n')


if __name__ == '__main__':
    main()
