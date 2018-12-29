#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import  json
import requests
import chardet
from idna import unicode
from lib import  manage_string

class Dingding():
    def __init__(self,url,headers):
        self.url = url
        self.HEADERS = headers
    def post_text(self, Msg):
        dict_textMsg = {'msgtype':'text'}
        manage_string.dict_u8_to_unicode(Msg)
        #dict_textMsg["text"] = Msg
        #print(unicode(dict_textMsg["text"]["title"], "utf-8"))
        #data = json.dumps(dict_textMsg.decode('UTF-8'))
        #print(data)
        #print (chardet.detect(data))
        #res = requests.post(url=self.url, data=data, headers=self.HEADERS)
        #print(res.text)

