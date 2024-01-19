from unittest import TestCase
from main import codes_names
from main2 import top_3
from main3 import pairs_names_dict
from yandexmain import *
import requests
token = 'y0_AgAAAAAvEey6AADLWwAAAADlWfR8HYm-RX-DQNCzpKbftyac9q6G0-E'
uploader = YaUploader(token)


class Testnames(TestCase):
    def test_names(self):
        first = ['Адилет', 'Азамат', 'Денис', 'Евгений', 'Ринат', 'Роман', 'Сергей']
        expected = codes_names[1]
        self.assertEqual(first, expected)

    def test_top3(self):
        expected = 10
        self.assertEqual(expected, top_3[0][1])

    def test_pairs_names(self):
        result = pairs_names_dict['Python-разработчик с нуля', 'Java-разработчик с нуля']
        expected = ['Антон', 'Евгений', 'Максим']
        self.assertEqual(result, expected)

    def test_yandex(self):
        result = uploader.create_folder('First test')
        code = result.status_code
        expected = 201
        self.assertEqual(expected, code)

    def test_yandex_failure(self):
        result = uploader.create_folder('123')
        code = result.status_code
        expected = 201
        self.assertEqual(expected, code) # Тест провалится так как у меня на яндекс диске уже есть такая папка

    def test_yandex_nums(self):
        result = uploader.create_folder(asdsak123894123)
        code = result.status_code
        expected = 200
        self.assertEqual(expected, code)