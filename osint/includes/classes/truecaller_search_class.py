import requests

class Truecaller:
    def truecaller_search(self):
        turl = "https://search5-noneu.truecaller.com/v2/search?q=" + self.num + "&countryCode=IN&type=4&locAddr=&placement=SEARCHRESULTS%2CHISTORY%2CDETAILS&encoding=json"
        theaders = {
                "user-agent": "Truecaller/11.5.7 (Android;10)",
                "Accept-Encoding": "gzip",
                "authorization": self.token,
                "Host": "search5-noneu.truecaller.com"
            }
        tresponse = requests.get(turl, headers=theaders, timeout=5)

        return tresponse
    def __init__(self, num, token):
        self.num = num
        self.token = token
token ="Bearer a1i0R--QULj06V5kbAlVPy_aynMfCnoUHbndb2k01j2bzL9nMP1y8Ti1a5o5xNle"
num = "9048903190"
true_caller_result = Truecaller(num, token)
output = true_caller_result.truecaller_search()
print(output.text)


