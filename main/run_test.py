#coding=utf-8
from Base.run_method import RunMethod
from Data.get_Data import GetData
from Unit.common_unit import CommonUnit


class RunTest:
    def __init__(self):
        self.data = GetData()
        self.common = CommonUnit()
        self.run_method = RunMethod()


     #程序入口
    def  go_to_run(self):
        res =None
        rows_count = self.data.get_case_line();
        for i in range(1,rows_count):
            print i
            is_run = self.data.get_is_run(i)
            method = self.data.get_request_way(i)
            url =self.data.get_url(i)
            request_data = self.data.get_request_data(i)
            header = self.data.is_header(i)
            exepct = self.data.get_expect_data(i)
            if is_run ==True:
                res = self.run_method.run_main(method,url,request_data,header)
                if self.common.is_contain(exepct,res):
                    self.data.write_result(i,"pass")
                else:
                    self.data.write_result(i,'fail')

