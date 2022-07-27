#爬取某贴吧前十页源码下载
import requests, os

base_url = 'https://tieba.baidu.com/f?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}

dirname = './tieba/woman/'
#os.path.exists()  文件或者路径是否存在  返回True/False
if not os.path.exists(dirname):
    os.makedirs(dirname)
for i in range(0, 10):
    params = {
        'ie': 'utf-8',
        'kw': '美女',
        'pn': str(i * 50)
    }
    response = requests.get(base_url, headers=headers, params=params)
    #使用with open() as file的格式，目的是在对文件操作之后接着关闭文件，防止长时间占用内存
    with open(dirname + '美女第%s页.html' % (i + 1), 'w', encoding='utf-8') as file:
        file.write(response.content.decode('utf-8'))
    print('第{}页完成'.format(i))

