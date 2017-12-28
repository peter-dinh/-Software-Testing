import requests
import json


def post():
    url = 'http://localhost:51717/token'
    data = {'username': 'thuan@gmail.com', 'password': '123456', 'grant_type': 'password'}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    data_json = json.dumps(data)
    return requests.post(url, data, headers).json()

def get():
    url = 'http://localhost:51717/api/Products/SearchProduct'
    payload = {'brandId': '1'}
    return requests.get(url, params=payload)

def ListProductInCart(token):
    url = 'http://localhost:51717/api/Cart/ViewCart'
    headers = {'contentType': 'application/json', 'Authorization': "Bearer " +token}
    return requests.get(url, headers).json()

if __name__ == '__main__':
    print(post().json())

   

