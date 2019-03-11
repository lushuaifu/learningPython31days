import time


# def application():
#     return time.ctime()


def application(env, startResponse):
    '''
     这个方法功能：设置响应的状态码和响应的响应头和返回响应体
    :param env:
    :param startResponse:
    :return: 响应体
    '''
    status = 'HTTP/1.1 200 OK'
    responseHeaders = [('Server','laowang'),('Date','Tue Jun 20 14:32:26 2017'),('Content-Type','text/plain')]

    startResponse(status,responseHeaders)

    responseBody = str(time.ctime())
    return responseBody
