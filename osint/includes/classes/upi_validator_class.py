import requests
import json

class UpiValidator:
    def VpaValidator(self):        
        turl = "https://api.juspay.in/upi/verify-vpa"
        theaders = {
       "X-Jp-Merchant-Id": "vodafone_web",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json, text/plain, */*",
        "X-Merchantid": "vodafone_web",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "alive",        
             }

        data = {
        'vpa': self.vpa+'@'+self.upi,
        'merchant_id': 'vodafone_web'
              }
        tresponse = requests.post(turl, headers=theaders,data=data)

        return tresponse
    def __init__(self, vpa, upi):
        self.vpa = vpa
        self.upi = upi







