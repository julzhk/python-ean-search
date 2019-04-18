"""
A Python class for EAN and ISBN name lookup and validation using the API on ean-search.org.
To use it, you need an API access token from https://www.ean-search.org/ean-database-api.html
This version Python 3.6+ only
"""

import requests

class EANSearch:

    def __init__(self, token, lang=1):
        self.token = token
        self.lang = lang
        self.base_url = f"https://api.ean-search.org/api?token={self.token}&format=json&lang={self.lang}"

    def do_json_request(self, url):
        response = requests.get(url,
                                headers={
                                    'cache-control': "no-cache"
                                })
        data = response.json()
        return data

    def barcodeLookup(self, ean):
        """Lookup the product name for an EAN barcode"""
        data = self.do_json_request(f"{self.base_url}&op=barcode-lookup&ean={ean}")
        if "error" in data[0]:
            return None
        else:
            return data[0]["name"]


    def verifyChecksum(self, ean):
        """verify checksum of an EAN barcode"""
        data = self.do_json_request(f"{self.base_url}&op=verify-checksum&ean={ean}")
        try:
            return data[0]["valid"]
        except (IndexError, KeyError):
            return None

    def productSearch(self, name, page=0):
        """search for a product name"""
        data = self.do_json_request(f"{self.base_url}&op=product-search&name={name}&page={page}")
        return data["productlist"]

    def barcodePrefixSearch(self, prefix, page=0):
        """search for a prefix of EAN barcodes"""
        data = self.do_json_request(f"{self.base_url}&op=barcode-prefix-search&prefix={prefix}&page={page}")
        return data["productlist"]


