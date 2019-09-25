import requests
import re
import json


class SpidersXing():
    def __init__(self, url):
        self.url = url
        self.start_url = 'https://whois.aliyun.com/whois/domain/{}'.format(url)
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        }

    def parse_all(self):
        session = requests.session()

        res_text = session.get(url=self.start_url, headers=self.headers).text
        umToken = re.findall(r"var umToken=\'(.*?)\';", res_text, re.S)[0]
        url = 'https://whois.aliyun.com/whois/api_whois_info?domainName={}&umToken={}'.format(self.url, umToken)
        json_text = session.get(url=url, headers=self.headers).text
        data_text = json.loads(json_text)
        data = data_text.get("module").get("originalInfo")
        return data


if __name__ == '__main__':
    s = SpidersXing('aliyun.com')
    data = s.parse_all()
    print(data)
