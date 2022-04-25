from xmrAPI import *




# How to pass custom remote host and port
# host = "192.168.1.123"
# port = "1234"
# api = xmrAPI(host, port)



# Defaults to localhost port 1010 if not passed
api = xmrAPI()



summary = api.getSummary()
pool = summary["connection"]["pool"]
hashrate = summary["hashrate"]["total"]
uptime = summary["uptime"]

print(hashrate[0])
