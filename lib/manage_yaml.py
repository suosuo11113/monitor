#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import yaml

class manage_yaml:
    def __init__(self,yaml_file):
        self.yaml_file = yaml_file


    def jiexi_yaml(self):
        with open(self.yaml_file ,'r', encoding='UTF-8') as f:
            msg_yaml = yaml.load(f)
        return  msg_yaml
