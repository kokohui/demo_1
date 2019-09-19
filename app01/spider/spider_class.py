import requests
import re
import json


class SpidersXing():
    def __init__(self, start_url):
        self.start_url = start_url
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        self.item = {}

    def parse_all(self):

        res_text = requests.get(url=self.start_url, headers=self.headers).text
        json_text = re.findall('window.pageData=(.*?)</script>', res_text, re.S)[0]
        data_text = json.loads(json_text)

        tips_all = data_text["mods"]["resultTips"]["tips"]
        tips = tips_all.split(' ')[0]
        return tips

    def parse_xing(self):
        item = self.item
        item['tips'] = self.parse_all()
        for num in range(1, 6):
            xing_url = self.start_url + '?rating={}'.format(num)
            print('xing_url:', xing_url)
            res_text = requests.get(url=xing_url, headers=self.headers).text
            json_text = re.findall('window.pageData=(.*?)</script>', res_text, re.S)[0]
            data_text = json.loads(json_text)

            item['tips_' + str(num)] = data_text["mods"]["resultTips"]["tips"].split(' ')[0]
        return item


def main(start_url):
    spider = SpidersXing(start_url)
    item = spider.parse_xing()
    print(item)


if __name__ == '__main__':
    main('https://www.lazada.com.my/shop-mobiles/')
