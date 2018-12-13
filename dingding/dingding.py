#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import  json
import requests
class dingding():
    def __init__(self,url ,headers):
        self.url = url
        self.HEADERS = headers
    def post_text(self,String_Msg):
        String_textMsg = {
            "msgtype": "text",
            "text": {
            "content": 'kind:%s\naverage:%f\nmedian:%f\nQ10:%f\nQ90:%f' % ("Trans", 2.23, 5.78, 99.2, 99.3)
            }
        }
        data = json.dumps(String_textMsg)
        res = requests.post(self.url, data=data, headers=self.HEADERS)
