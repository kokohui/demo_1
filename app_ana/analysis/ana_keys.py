import numpy as np


def price_key(list):
    price_data = {}
    list = [float(i) for i in list]
    list_arr = np.array(list)
    price_max = np.max(list_arr)
    price_min = np.min(list_arr)
    price_avg = np.mean(list_arr)
    price_data['max'] = round(float(price_max), 2)
    price_data['min'] = round(float(price_min), 2)
    price_data['avg'] = round(float(price_avg), 2)
    return price_data


def discount_key(lis):
    review_data = {}
    list = [float(i.replace('-', '').replace('%', '')) for i in lis if i != ''and i != 'None']
    print(list)
    list_arr = np.array(list)
    review_max = np.max(list_arr)
    review_min = np.min(list_arr)
    review_avg = np.mean(list_arr)
    review_data['max'] = str(round(float(review_max), 2)) + '%'
    review_data['min'] = str(round(float(review_min), 2)) + '%'
    review_data['avg'] = str(round(float(review_avg), 2)) + '%'
    return review_data


def seller_len(lis):
    seller_list = [i for i in lis if i != []]
    sum_con = len(list(set(seller_list)))
    return sum_con


def deliver(list):

    item = str(round(list.count('China')* 100 /len(list), 2)) + '%'

    return item