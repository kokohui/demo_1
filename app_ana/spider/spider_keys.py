import requests
import re
import json
from lxml import etree


class SpidersShop():
    def __init__(self, page, start_url):
        self.start_url = 'https://www.lazada.com.my/catalog/?_keyori=ss&from=input&page={}&q={}'.format(str(page), str(start_url))
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        self.item = {}

    def parse_all(self):

        # item = self.item
        print('start_url:', self.start_url)
        res_text = requests.get(url=self.start_url, headers=self.headers).text
        print(res_text)
        json_text = re.findall('window.pageData=(.*?)</script>', res_text, re.S)[0]
        data_text = json.loads(json_text)
        # print(data_text)

        pro_url_list = []
        url_list = re.findall(r'(//www.lazada.com.my/products/.*?)\"', res_text, re.S)
        url_list = list(set(url_list))
        for url in url_list:
            pro_url = 'https:' + url
            pro_url_list.append(pro_url)

        price_list = []
        review_list = []
        discount_list = []
        listItems = data_text["mods"]["listItems"]
        for item in listItems:
            price = item.get("price")
            review = item.get("review")
            discount = item.get("discount")


            price_list.append(price)
            review_list.append(review)
            discount_list.append(str(discount))

        self.item['price_list'] = price_list
        self.item['review_list'] = review_list
        self.item['discount_list'] = discount_list
        self.item['pro_url_list'] = pro_url_list

        return self.item

    def parse_detail(self):
        item = self.parse_all()

        percentRate_list = []
        sellerName_list = []
        address_list = []
        detail_url_list = item.get('pro_url_list')
        print(detail_url_list)

        for detail_url in detail_url_list:
            res_text = requests.get(url=detail_url, headers=self.headers).text

            percentRate = ''
            try:
                percentRate = re.findall(r'\"percentRate\":\"(.*?)\"', res_text, re.S)[0]
                print(percentRate)
            except:
                print(percentRate)

            sellerName = ''
            try:
                sellerName = re.findall(r'\"sellerName\":\"(.*?)\"', res_text, re.S)
                if sellerName != []:
                    sellerName = sellerName[0]
                    sellerName_list.append(sellerName)
            except:
                print(sellerName)

            address = ''
            try:
                address = re.findall(r'\"address\":\"(.*?)\"', res_text, re.S)[0]
            except:
                print(address)

            percentRate_list.append(percentRate)
            sellerName_list.append(sellerName)
            address_list.append(address)

        item['percentRate_list'] = percentRate_list
        item['sellerName_list'] = sellerName_list
        item['address_list'] = address_list

        return item

    # def parse_con(self, res_text):
    #     sisUrl = re.findall(r'\"sisUrl\":\"(.*?)\"', res_text, re.S)[0]
    #     sisUrl = 'https:' + sisUrl.split('?')[0] + '?langFlag=en&path=profile.htm&pageTypeId=3'
    #     print('sisUrl:', sisUrl)
    #
    #     con_text = requests.get(url=sisUrl, headers=self.headers).content
    #     con_text = con_text.decode()
    #
    #     with open('kk.html', 'w', encoding='utf-8') as f:
    #         f.write(con_text)
    #     num_list = re.findall(r'background-color: rgb\(0, 62, 82\)', con_text, re.S)
    #     print('num_list:', num_list)


def main(page, start_url):

    item = []

    for num in range(1, page):
        spider = SpidersShop(page, start_url)
        item_pag = spider.parse_detail()
        item.append(item_pag)

    return item


if __name__ == '__main__':
    main(2, 'headset')

'whois-web-hichina-com:48ee70c093186e9b31c83ecf178c96f5'