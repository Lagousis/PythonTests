from pathlib import Path
import os
from types import SimpleNamespace
import json
import redis
import hashlib

def readConfig():
    configFilePath = Path(os.getcwd()).parent / "credentials.json"
    print(f"Reading config file from {configFilePath}")

    args = SimpleNamespace()

    with open(configFilePath) as f:
        data = json.load(f)['redis']
        args.hostname = data['hostname']
        args.key = data['key']
    return args

args = readConfig()

myHostname = args.hostname
myPassword = args.key

params = {'host'}

r = redis.StrictRedis(host=myHostname, port=6380,
                      password=myPassword, ssl=True)

result = r.ping()
print("Ping returned : " + str(result))

key_info = {}
key_info['companyid'] = "eqweqwe"
key_info['mainuser'] = "Stavros"

#r.set("key1", key_info)

# for key in key_info.keys():
#     r.hset("key1", key, key_info[key])

#r.hset("key1", mapping=key_info)
#r.expire("key1", time=25)

#print(r.exists("key1")==1)

#print(r.hgetall("key1"))
print(r.keys())

apikey_info = r.hgetall("b4bca39818ed264a9b5a6e0b0865a7230fe0ce31d1e88fdf19ea32229c6ee8cc")

print(apikey_info)

print(apikey_info[b'companyid'])

# key = 'dFdGXlRJGqjehCxBq4tLKSYFgiKwC0tCWsbWEY9BAUs='

# m = hashlib.sha256()
# m.update("Stavros".encode())
# m.update(key.encode())

# print(m.hexdigest())