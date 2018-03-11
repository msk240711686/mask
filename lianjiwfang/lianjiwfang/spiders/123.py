import requests

# GD_location_url = 'http://restapi.amap.com/v3/geocode/geo?key={}&address={}&city={}'.format(
#     self.GD_location_key, detail, self.City)
url = 'http://restapi.amap.com/v3/geocode/geo?key=b8805f96e2369575ba8e3bc8c3624919&address=成都信息工程大学航空港校区A&city=成都'
result = requests.get(url)
result = result.text
print(type(result))
result = eval(result)
print(result['status'],type(result['status']))
if result['status'] == "1":
    print(result['geocodes'])
    print(result['geocodes'][0])
    print(result['geocodes'][0]['location'])
    k = result['geocodes'][0]['location']
    print(type(k))
    k = k.split(',')
    print(k[0],k[1])
    print('123')