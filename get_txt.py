import requests

url = 'https://blog.csdn.net/weixin_33733810/article/details/89731244'
r = requests.get(url)

print(r.encoding)
print(r.text)
r.encoding = r.apparent_encoding
print(r.encoding)
print(r.text)