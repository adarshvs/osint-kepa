from urllib import request, parse
import json
import requests
import json

class HlrLookup:
    def HlrLookupNeutrinoapi(self):        
        url = 'https://neutrinoapi.net/hlr-lookup'
        params = {
        'user-id': self.user_id,
        'api-key': self.api_key,
        'number': self.num
        }
        postdata = parse.urlencode(params).encode()
        req = request.Request(url, data=postdata)
        response = request.urlopen(req)
        result = json.loads(response.read().decode("utf-8"))
        
        return result
    def __init__(self, user_id, api_key, num):
        self.user_id = user_id
        self.api_key = api_key        
        self.num = num


