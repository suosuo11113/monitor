#!/usr/bin/env python
import dns.resolver

domain = 'www.baidu.com'

A = dns.resolver.query(domain, 'A')
for i in A.response.answer:
    for j in i.items:
        print (j)
