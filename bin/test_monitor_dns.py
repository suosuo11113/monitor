#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from lib.monior_dns import dns_monitor

if __name__ == '__main__':
    dns1 = dns_monitor('../conf/dns.conf')
    dns1.get_iplist_A()
    dns1.check_ip()

