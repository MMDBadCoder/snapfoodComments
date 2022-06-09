# using https://curlconverter.com/


import json
from concurrent.futures import ThreadPoolExecutor

import requests


class Curler:

    def __init__(self):
        self.min_empty_page_number = 1000
        self.extracted_comments = []

    def extract_comments_by_page_number(self, params):
        page_number = params['page']
        page_number = int(page_number)
        if page_number > self.min_empty_page_number:
            return

        headers = {
            'authority': 'snappfood.ir',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
            'content-type': 'application/x-www-form-urlencoded',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        }

        response = requests.get('https://snappfood.ir/mobile/v1/restaurant/vendor-comment', params=params,
                                headers=headers)

        extracted_data = json.loads(response.content)
        comments = extracted_data['data']['comments']

        if len(comments) == 0:
            self.min_empty_page_number = page_number
        else:
            self.extracted_comments += comments
            print("Page " + str(page_number) + " was curled")

    def extract_all_comments(self, vendor_code):
        params_list = []
        for i in range(1000):
            params = {
                'vendorCode': vendor_code,
                'page': str(i),
            }
            params_list.append(params)

        with ThreadPoolExecutor(max_workers=10) as exe:
            result = exe.map(self.extract_comments_by_page_number, params_list)

        return self.extracted_comments
