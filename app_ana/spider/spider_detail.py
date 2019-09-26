import requests
import re
import json


class SpidersXing2():
    def __init__(self, start_url):
        self.start_url = start_url
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        self.item = {}

    def parse_xing_2(self):
        pro_url_list = []

        xing_url = self.start_url
        print('xing_url:', xing_url)
        res_text = requests.get(url=xing_url, headers=self.headers).text
        data = {}
        url_list = re.findall(r'(//www.lazada.com.my/products/.*?)\"', res_text, re.S)
        url_list = list(set(url_list))
        for url in url_list:
            pro_url = 'https:' + url
            data['pro_url'] = 'pro_url'
            pro_url_list.append(pro_url)
        self.item['pro_url_list'] = pro_url_list

        return self.item

    def parse_pro_2(self):
        item = self.parse_xing_2()
        url_list = item.get('pro_url_list')[:10]
        dataList = []
        for url in url_list:

            res_text = requests.get(url=url, headers=self.headers).text
            con_home = re.findall(r'\"sisUrl\":\"(.*?)\"', res_text, re.S)[0]
            con_home_url = 'https:' + con_home.split('?')[0] + '?langFlag=en&path=profile.htm'
            print('con_home_url:', con_home_url)
            profile_text = requests.get(url=con_home_url, headers=self.headers).text
            con_data_json_url = 'https:' + re.findall(r"window.shopPageDataApi = \'(.*?)\'", profile_text, re.S)[0]
            con_data_json = requests.get(con_data_json_url, headers=self.headers).text

            data_dict = self.parse_detail(res_text, con_data_json, con_home_url)

            print(data_dict)
            dataList.append(data_dict)

        self.item['commodityInfo'] = dataList
        del self.item['pro_url_list']
        return item

    def parse_detail(self, res_text, con_data_json, con_home_url):
        data = {}
        brand = ''
        try:
            brand = re.findall(r'\"brand\":{\"name\":\"(.*?)\"', res_text, re.S)[0]
        except:
            print('空')

        title = ''
        try:
            title = re.findall(r'<title>(.*?)</title>', res_text, re.S)[0]
        except:
            print('空')

        price = ''
        try:
            price = re.findall(r'\"salePrice\":{\"text\":\".*?\","value":(.*?)}', res_text, re.S)[0]
        except:
            print('空')

        evaNum = 0
        try:
            evaNum = re.findall(r'\"rating\":{\"score\":.*?,\"total\":(.*?)}', res_text, re.S)[0]
        except:
            print('空')

        score = 0
        try:
            score = re.findall(r'\"rating\":{\"score\":(.*?),\"total\":.*?}', res_text, re.S)[0]
        except:
            print('空')

        percentRate = 0
        try:
            percentRate = re.findall(r'\"percentRate\":\"(.*?)\"', res_text, re.S)[0]
        except:
            print('空')

        proUrl = ''
        try:
            proUrl = re.findall(r'\[{\"poster\":\"(.*?)\"', res_text, re.S)[0]
            proUrl = 'https:' + proUrl
        except:
            print('空')

        location = ''
        try:
            location = re.findall(r'\"location\":\"(.*?)\"', con_data_json, re.S)[0]
        except:
            print('空')

        keepTime = ''
        try:
            keepTime = re.findall(r'\"keepTime\":\"(.*?)\"', con_data_json, re.S)[0]
        except:
            print('空')

        shopSize = ''
        try:
            shopSize = re.findall(r'\"shopSize\":\"(.*?)\"', con_data_json, re.S)[0]
        except:
            print('空')

        sellerKey = ''
        try:
            sellerKey = re.findall(r'\"sellerKey\":\"(.*?)\"', con_data_json, re.S)[0]
        except:
            print('空')

        shopRating = ''
        try:
            shopRating = re.findall(r'\"shopRating\":\"(.*?)\"', con_data_json, re.S)[0]
            shopRating = shopRating.split(' ')[0]
        except:
            print('空')

        data['brand'] = brand
        data['title'] = title
        data['price'] = price
        data['evaNum'] = evaNum
        data['score'] = score
        data['percentRate'] = percentRate
        data['proUrl'] = proUrl

        data['location'] = location
        data['keepTime'] = keepTime
        data['shopSize'] = shopSize
        data['sellerKey'] = sellerKey
        data['shopRating'] = shopRating
        data['con_home_url'] = con_home_url

        return data


def main2(start_url):
    spider = SpidersXing2(start_url)
    item = spider.parse_pro_2()
    print('总信息:', item, "结束了!!")


if __name__ == '__main__':
    main2('https://www.lazada.com.my/shop-mobiles/')
