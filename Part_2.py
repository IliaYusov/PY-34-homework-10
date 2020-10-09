import requests
import os
import sys


class YaUploader:
    API_URL = 'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        kwargs = {'path': '/' + file_path.rsplit(os.path.sep)[-1]}
        endpoint = '/upload'
        auth_header = {'Authorization': self.token}
        upload_response = requests.get(YaUploader.API_URL + endpoint, headers=auth_header, params=kwargs)
        upload_response.raise_for_status()
        with open(file_path, 'rb') as f:
            response = requests.put(upload_response.json()['href'], f)
            response.raise_for_status()
        return response.status_code


if __name__ == '__main__':
    if len(sys.argv) == 2:
        file_ = sys.argv[1]
        uploader = YaUploader('<TOKEN>')
        try:
            result = uploader.upload(file_)
            if result == 201:
                print(f'{file_.rsplit(os.path.sep)[-1]} uploaded successfully')
            else:
                print(f'Something gone wrong. Status code: {result}')
        except requests.HTTPError as error:
            print(error)
        except FileNotFoundError:
            print('File not found')
    else:
        print(f'Script uses only one argument, but {len(sys.argv) - 1} were given')
