import requests
import json
class Darknet:
    def darknet_search(self):
        turl = "https://darksearch.io/api/search?query=" + self.keyword 
        theaders = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90",
                "Accept-Encoding": "gzip",
                "Host": "darksearch.io",
                "Connection": "close"
            }
        tresponse = requests.get(turl, headers=theaders, timeout=5)

        return tresponse
    def __init__(self, keyword):
        self.keyword = keyword
        

