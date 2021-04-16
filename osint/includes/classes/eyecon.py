
import requests

class Eyecon:
    def eyecon_search(self):
        
        turl ="https://api.eyecon-app.com/app/getnames.jsp?cli=91"+ self.num +"&lang=en&is_callerid=true&is_ic=true&cv=vc_365_vn_3.0.365_a&requestApi=URLconnection&source=Other"
        theaders = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "accept": "application/json",
                    "e-auth-v": "e1",
                    "e-auth": self.token,
                    "e-auth-c": "43",
                    "e-auth-k": "PgdtSBeR0MumR7fO",
                    "e-checksum": "ZIv8tFHeLh4aVa0c7nu3/DMLtKc=",
                    "accept-charset": "UTF-8",
                    "content-type" : "application/x-www-form-urlencoded; charset=utf-8",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip" }
        tresponse = requests.get(turl, headers=theaders)
        return tresponse
    def eyecon_img_search(self):
        
        turl ="https://api.eyecon-app.com/app/pic?cli=91"+ self.num +"&is_callerid=true&size=big&type=0&cancelfresh=0&cv=vc_312_vn_2.0.312_a"
        theaders = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                    "accept": "application/json",
                    "e-auth-v": "e1",
                    "e-auth": self.token,
                    "e-auth-c": "43",
                    "e-auth-k": "PgdtSBeR0MumR7fO",
                    "e-checksum": "ZIv8tFHeLh4aVa0c7nu3/DMLtKc=",
                    "accept-charset": "UTF-8",
                    "content-type" : "application/x-www-form-urlencoded; charset=utf-8",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip" }
        timgresponse = requests.get(turl, headers=theaders)
        return timgresponse


    def __init__(self, num, token):
        self.num = num
        self.token = token


token ="c4664ab6-6202-4bb2-8ac5-dbd8bfbd5861"
num = "9995432221"

eyecon_result = Eyecon(num, token)
name = eyecon_result.eyecon_search()
imgresp = eyecon_result.eyecon_img_search()

fbrslt = imgresp.url.replace('https://graph.', '').replace('picture?width=600', '')
print(name.text)
print(fbrslt)