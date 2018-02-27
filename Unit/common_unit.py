#coding:utf-8

class CommonUnit:

    def is_contain(self,str_one,str_two):
        str_one = str_one.encode('unicode-escape').decode('string-escape')
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag