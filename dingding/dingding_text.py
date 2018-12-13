#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import json
import requests
if __name__ == '__main__':
    url = 'https://oapi.dingtalk.com/robot/send?access_token=b73d4f6441b3ea0e867350fec9b0e430d9c8d4fef8a792776c66fe10db35cad1'
    HEADERS = {"Content-Type": "application/json;charset=utf-8"}
    String_textMsg={"msgtype":"text","text":{"content":'kind:%s\naverage:%f\nmedian:%f\nQ10:%f\nQ90:%f'%("Trans",2.23,5.78,99.2,99.3)}}

    String_textMsg=json.dumps(String_textMsg)

    res=requests.post(url,data=String_textMsg,headers=HEADERS)

    print(res.text)