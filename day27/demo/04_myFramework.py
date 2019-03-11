'''
自定义的符合wsgi的框架
'''
import time


class Application(object):
    def __init__(self, urls):
        '''框架初始化的时候需要获取路由列表'''
        self.urls = urls

    def __call__(self, env, startResponse):
        '''
        判断是静态资源还是动态资源。
        设置状态码和响应头和响应体
        :param env:
        :param startResponse:
        :return:
        '''
        # 从请求头中获取文件名
        fileName = env.get('PATH_INFO')

        # 判断静态还是动态
        if fileName.startwith('/static'):
            fileName = fileName[7:]
            if '/' == fileName:
                filePath += '/index.html'
            else:
                filePath += fileName
            try:
                file = None
                file = open(filePath, 'r', encoding='gbk')
                responseBody = file.read()
                status = 'HTTP/1.1 200 OK'
                responseHeaders = [('Server', 'laowang')]

            except FileNotFoundError:
                status = 'HTTP/1.1 404 Not Found'
                responseHeaders = [('Server', 'laowang')]
                responseBody = '<h1>找不到<h1>'
            finally:
                startResponse(status, responseHeaders)
                if (file != None) and (not file.closed):
                    file.close()
        else:
            isHas = False  # 表示请求的名字是否在urls中，True:存在，False：不存在
            for url, func in self.urls:
                if url == fileName:
                    responseBody = func(env, startResponse)
                    isHas = True
                    break
            if isHas == False:
                status = 'HTTP/1.1 404 Not Found'
                responseHeaders = [('Server', 'laowang')]
                responseBody = '<h1>找不到<h1>'
                startResponse(status, responseHeaders)
        return responseBody


def mytime(env, startResponse):
    status = 'HTTP/1.1 200 OK'
    responseHeaders = [('Server', 'time')]
    startResponse(status, responseHeaders)
    responseBody = str(time.ctime())
    return responseBody




def mynews(env, startResponse):
    status = 'HTTP/1.1 200 OK'
    responseHeaders = [('Server', 'news')]
    startResponse(status, responseHeaders)
    responseBody = str('xx新闻')
    return responseBody


'''路由列表'''
urls = [
    ('/mytime', mytime),
    ('/mynews', mynews)
]

application = Application(urls)

