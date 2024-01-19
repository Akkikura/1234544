import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self,path):
        main_url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
        headers = self.get_headers()
        response = requests.put(f'{main_url}?path={path}', headers=headers)
        return response

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = 'y0_AgAAAAAvEey6AADLWwAAAADlWfR8HYm-RX-DQNCzpKbftyac9q6G0-E'
    uploader = YaUploader(token)

    result = uploader.create_folder('asdsada')