#coding=utf-8
from Base.run_method import RunMethod
from Data.get_Data import GetData
from Unit.common_unit import CommonUnit
from Unit.dependdent_data import DeppenddentData


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
            depend_case =self.data.is_depend(i)
            if depend_case!=None:
                self.depend_data = DeppenddentData()
                depend_response_data=self.depend_data.get_data_for_key(i)
                depend_key  = self.data.get_depend_filed(i)
                request_data[depend_key] = depend_response_data

            res = self.run_method.run_main(method,url,request_data,header)

            if is_run ==True:

                if self.common.is_contain(exepct,res):
                    self.data.write_result(i,"pass")
                else:
                    self.data.write_result(i,'fail')


if __name__ == '__main__':

    run = RunTest()
    data= run.go_to_run()