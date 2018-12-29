#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import  difflib
import  sys

def readline(filename):
    try:
        f = open(filename,'r')
        text = f.read().splitlines()
        f.close()
    except IOError as error:
        print("read file error:",str(error))
        sys.exit()
    return  text
if __name__ == '__main__':
    text1 = "../data/text1"
    text2 = "../data/text2"

    text1_lines = readline(text1)
    text2_lines = readline(text2)
    print('\n'.join(text2_lines))
    d = difflib.HtmlDiff()
    #print(d.make_file(text1_lines,text2_lines))
    with open("../data/diff_file1.html",'w') as f:

       f.write(d.make_file(text1_lines,text2_lines))
       f.close()


