import requests




# Based on the documentation on https://xmrig.com/docs/miner/api/config
# r = requests.get(f"http://{host}:{port}/{apiVer}/{endpoint}")
class xmrAPI:
    def __init__(self,_host = '127.0.0.1',_port = '1010'):
        self.VERSION = "0.0.1"
        self.host = _host
        self.port = _port
        self.apiVer = 2
        self.url = {
        "summary":f"http://{self.host}:{self.port}/{self.apiVer}/summary",
        "backends":f"http://{self.host}:{self.port}/{self.apiVer}/backends",
        "config":f"http://{self.host}:{self.port}/{self.apiVer}/config",
        "json_rpc":f"http://{self.host}:{self.port}/json_rpc"
        }
    def getJson(self,_endpoint):
        endpoint = self.url[_endpoint]
        r = requests.get(endpoint)
        status = r.status_code
        if status == 200:
            return r.json()
        else:
            return False
    def getSummary(self):
        return self.getJson("summary")
    def getBackends(self):
        return self.getJson("backends")
    def getConfig(self):
        return self.getJson("config")



# Class for loops and checking status
class WatcherProcess:
    def __init__(self):
        self.alive = False
    def initiate(self):
        self.alvie = True
    def kill(self):
        self.alvie = False
    def isAlive(self):
        return self.alive
