#coding=utf-8
import json


class OperationJson:

    def __init__(self):
        self.data = self.read_json()

    #读取json文件
    def read_json(self):
        with open("../dataConfig/data.json") as fp:
             data =json.load(fp)
        return data

    #读取json中的详细数据
    def get_data(self,id):
         return self.data[id];


if  __name__ =='__main__':
    oper = OperationJson();
    print oper.get_data("loginout");