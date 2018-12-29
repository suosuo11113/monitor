#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import  filecmp

if __name__ == '__main__':
    text1 = "../data/text1"
    text2 = "../data/text2"

    #print(filecmp.cmp(text1,text1,False))
    print(filecmp.dircmp("../data","../data",["text1","text2"]).report())
