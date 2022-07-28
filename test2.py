from urllib import request,parse

def get_url(word):
    '''拼url地址'''
    url = 'http://www.baidu.com'
    full_url = url.format()
    return full_url

def request_url(full_url,filename):
    '''发请求l,保存本地'''
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
    req = request.Request(url=full_url,headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    with open(filename,'w',encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    word = input('请输入搜索内容：')
    url = get_url(word)
    filename = word + '.html'
    request_url(url,filename)