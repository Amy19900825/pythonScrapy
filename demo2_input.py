import requests

#TODO 链接从哪儿来？headers的东西从哪儿来？

base_url = 'https://fanyi.baidu.com/sug'
kw = input('请输入要翻译的英文单词：')
data = {
    'kw': kw
}
headers = {
    'content-length': str(len(data)),
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'referer': 'https://fanyi.baidu.com/',
    'x-requested-with': 'XMLHttpRequest'
}
response = requests.post(base_url, headers=headers, data=data)
# print(response.json())
# 结果：{'errno': 0, 'data': [{'k': 'python', 'v': 'n. 蟒; 蚺蛇;'}, {'k': 'pythons', 'v': 'n. 蟒; 蚺蛇;  python的复数;'}]}

# -----------------------------把结果隔行输出
result = ''
#response.json()返回结果的JSON对象(如果结果是以JSON格式编写的，否则返回错误)
for i in response.json()['data']:
    result += i['v'] + '\n'

print(kw + '的翻译结果为：')
print(result)

