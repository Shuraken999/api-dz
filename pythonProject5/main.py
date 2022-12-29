import requests
from settings import TOKEN


class YaUploader:
    def __init__(self, token_ya: str):
        self.token_ya = token_ya

    host = 'https://cloud-api.yandex.net/'

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token_ya}'}

    def upload(self, yadisk_file_name, get_link):
        requests.put(get_link, headers=self.get_headers(), data=open(yadisk_file_name, 'rb'))


if __name__ == '__main__':
    token = YaUploader(TOKEN)
    path_file_name = 'data.json'
    uri = 'v1/disk/resources/upload/'
    url = YaUploader.host + uri
    params = {'path': f'/{path_file_name}'}
    response = requests.get(url, headers=token.get_headers(), params=params)
    link = response.json()['href']
    token.upload(path_file_name, link)
    if response.status_code == 200:
        print(f'Файл загружен под именем "{path_file_name}"')

