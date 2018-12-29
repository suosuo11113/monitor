#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import json
import requests
if __name__ == '__main__':
    heard = {'Content-Type': 'application/json'}
    payload = "就是测试一下中文"
    r = requests.post("https://oapi.dingtalk.com/robot/send?access_token=b73d4f6441b3ea0e867350fec9b0e430d9c8d4fef8a792776c66fe10db35cad1", heards=heard, data=payload)