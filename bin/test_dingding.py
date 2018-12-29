from dingding import dingding
from lib import  manage_string

class MyTest():
    def test_dingding_text(self):
        #self.assertEqual(True, False)
        tokenid='b73d4f6441b3ea0e867350fec9b0e430d9c8d4fef8a792776c66fe10db35cad1'
        url = 'https://oapi.dingtalk.com/robot/send?access_token='+ tokenid
        HEADERS = {"Content-Type": "application/json;charset=utf-8"}
        manage_string.jiexi_yaml("../conf/dingding_template.yaml")
        #dd = dingding.Dingding(url=url,headers=HEADERS)
        #dd.post_text(data)




if __name__ == '__main__':
    mytest = MyTest()
    mytest.test_dingding_text()

