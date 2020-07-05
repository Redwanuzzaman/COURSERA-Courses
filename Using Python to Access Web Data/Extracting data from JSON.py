from urllib.request import urlopen
import json

address = input('Enter location: ')
data = urlopen(address).read().decode()
json_data = json.loads(data)

ans = 0
for item in json_data["comments"]:
    # print(item['count'])
    ans += int(item["count"])

print(ans)
