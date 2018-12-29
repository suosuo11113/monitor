#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import  os
import dns.resolver
from lib.manage_yaml import manage_yaml
class dns_monitor(manage_yaml):
    iplist = []   #定义域名Ip的列表变量

    def __init__(self,yaml_file):
        self.yaml_file = yaml_file
        self.domains = self.jiexi_yaml()

    def get_iplist_A(self):
        for i in self.domains:
            try:
                # print(i)
                A = dns.resolver.query(i,'A')
            except Exception :
                print("dns resolver fail")
                return False
            for x in A.response.answer: #通过response.answer的方法获取查询回应信息
                for j in x.items:
                    self.iplist.append(str(j))
            return  True

    def check_ip(self):
        for ip in self.iplist:
            print(ip)




