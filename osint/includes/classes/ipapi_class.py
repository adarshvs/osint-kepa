from requests import get

class IpLookup:

    def ip_lookup(self):
        loc = get('https://ipapi.co/'+ self.ip +'/json/')
        return loc

    def __init__(self, ip):
        self.ip = ip
