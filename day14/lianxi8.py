class shortinputException(Exception):
    def __init__(self,length,atleast):
        self.length=length
        self.atleast=atleast

def main():
    try:
123        if len(s)<3:
            raise shortinputException(len(s),3)
    except shortinputException as result:
        print('shortinputException:输入的长度是%d，长度至少应是%d'%(result.length,result.atleast))
    else:
        print('没用异常发生')
main()