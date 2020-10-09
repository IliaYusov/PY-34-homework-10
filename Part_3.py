import requests
import datetime

API_URL = 'https://api.stackexchange.com/2.2/questions'


def get_page(page):
    kwargs = {
        'page': page,
        'pagesize': 100,
        'order': 'desc',
        'sort': 'creation',
        'tagged': 'python',
        'site': 'stackoverflow',
        'fromdate': datetime.date.today() - datetime.timedelta(days=1)
    }
    r = requests.get(API_URL, params=kwargs)
    return r


questions_dict = {}
num = 0
has_more = True
while has_more:
    num += 1
    response = get_page(num)
    if 'error_id' in response.json():
        print(response.json()['error_message'])
        break
    has_more = response.json()['has_more']
    for item in response.json()['items']:
        questions_dict[item['title']] = item['link']

print(len(questions_dict))
