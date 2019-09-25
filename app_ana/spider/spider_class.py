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
        item_tip = {}
        pro_url_list = []
        item_tip['tips'] = self.parse_all()
        for num in range(1, 6):
            xing_url = self.start_url + '?rating={}'.format(num)
            print('xing_url:', xing_url)
            res_text = requests.get(url=xing_url, headers=self.headers).text
            json_text = re.findall('window.pageData=(.*?)</script>', res_text, re.S)[0]
            data_text = json.loads(json_text)
            item_tip['tips_' + str(num)] = data_text["mods"]["resultTips"]["tips"].split(' ')[0]

            data = {}
            url_list = re.findall(r'(//www.lazada.com.my/products/.*?)\"', res_text, re.S)
            url_list = list(set(url_list))
            for url in url_list:
                pro_url = 'https:' + url
                data['pro_url'] = 'pro_url'

                pro_url_list.append(pro_url)

        self.item['item_tip'] = item_tip
        self.item['pro_url_list'] = pro_url_list
        return self.item

    def parse_pro(self):
        item = self.parse_xing()
        url_list = item.get('pro_url_list')[:10]
        dataList = []
        for url in url_list:
            data = {}
            res_text = requests.get(url=url, headers=self.headers).text

            con_home = re.findall(r'\"sisUrl\":\"(.*?)\"', res_text, re.S)[0]
            con_home_url = 'https:' + con_home.split('?')[0] + '?langFlag=en&path=profile.htm'

            profile_text = requests.get(url=con_home_url, headers=self.headers).text
            con_data_json_url = 'https:' + re.findall(r"window.shopPageDataApi = \'(.*?)\'", profile_text, re.S)[0]
            con_data_json = requests.get(con_data_json_url, headers=self.headers).text

            brand = ''
            try:
                brand = re.findall(r'\"brand\":{\"name\":\"(.*?)\"', res_text, re.S)[0]
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
            except:
                print('空')

            data['brand'] = brand
            data['location'] = location
            data['keepTime'] = keepTime
            data['shopSize'] = shopSize
            data['sellerKey'] = sellerKey
            data['shopRating'] = shopRating
            data['con_home_url'] = con_home_url

            print(data)
            dataList.append(data)

        self.item['commodityInfo'] = dataList
        del self.item['pro_url_list']
        return item


def main(start_url):
    spider = SpidersXing(start_url)
    item = spider.parse_pro()
    print('总信息:', item, "结束了!!")


if __name__ == '__main__':
    main('https://www.lazada.com.my/shop-mobiles/')
