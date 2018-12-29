#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import  difflib
if __name__ == '__main__':
    text1 = '''
              text1:
    This is a difflib text1
    just for a test
    hahahha -7-1
    '''
    text2 = '''
              text2:
    This is a difflib text2
    just for a test
    hahahha -7-2
    '''

    text1_lines = text1.splitlines()
    text2_lines = text2.splitlines()

    '''d = difflib.Differ()
    diff = d.compare(text1_lines,text2_lines)
    print("\n".join(diff))'''

    d = difflib.HtmlDiff()
    with open ("../data/diff_file.html",'w') as f:
        f.write(d.make_file(text1_lines,text2_lines))
        f.close()
