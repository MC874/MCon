import requests
import os
import re

target = "line-optc.com"
temp = "testi.txt"
endpoint = "./debian-fs/root/Same/"
api_key = "e026829b-3190-40bb-a2ef-781cc054ddc4"

r = requests.get(f'https://api.builtwith.com/v19/api.json?KEY={api_key}&LOOKUP={target}')
jsun = r.json()
print(jsun, file=open(f"{target}.txt", "a"))

### RegEx Repository
with open(f"{target}.txt") as file:
	while (line := file.readline().rstrip()):
		uri = re.findall("://(.+?)\'", line)
		with open(temp, 'w') as f:
			for item in uri:
				f.write("%s\n" % item)
os.system(f"sed -i 's/\/.*//' {temp}")
os.system(f"sort -u {temp} >> {endpoint}{target}.txt")
os.system(f"rm -rf {temp} && rm -rf {target}.txt")