#coding:utf-8
from Unit.OperationExecl import OperationExecl
from Unit.OperationJson import OperationJson
from Data import data_config


class GetData:
    def __init__(self):
        self.oper_execl = OperationExecl()

    #获取case个数
    def get_case_line(self):
        return  self.oper_execl.get_rows()

    #获取是否运行
    def get_is_run(self,row):
        flag =None
        col = data_config.get_run()
        is_run = self.oper_execl.get_cell_value(row,col)
        if is_run=='yes':
            flag = True
        else:
            flag = False
        return flag

    #获取请求方式
    def get_request_way(self,row):
        col =data_config.get_run_way()
        request_way=self.oper_execl.get_cell_value(row,col);
        return  request_way

    #是否携带header
    def is_header(self, row):
        col = data_config.get_header_value()
        header = self.oper_execl.get_cell_value(row,col)
        if header != '':
            return header
        else:
            return None

     #获取url
    def get_request_url(self,row):
        col = data_config.get_url()
        url = self.oper_execl.get_cell_value(row,col)
        return url

    #获取请求数据
    def get_request_data(self,row):
        col = int(data_config.get_data())
        data = self.oper_execl.get_cell_value(row,col)
        if data =='':
            return None
        return data

    #通过获取关键字拿到data数据
    def get_data_for_json(self,row):
        oper_json =OperationJson()
        request_json = oper_json.get_data(self.get_request_data(row))
        return  request_json

    #获取预期结果
    def get_expect_data(self,row):
        col =int(data_config.get_expect())
        expect = self.oper_execl.get_cell_value(row,col)
        return expect

    #获取依赖数据的caseid
    def get_case_depend(self,row):
        col = int(data_config.get_case_depend())
        depend_case_id = self.oper_execl.get_cell_value(row,col)
        if depend_case_id =='':
            return  None
        else:
            return  depend_case_id

    #本case中依赖其他case返回的数据
    def get_response_data_depend(self,row):
        col = int(data_config.get_response_data_depend())
        depend_key = self.oper_execl.get_cell_value(row,col)
        if depend_key =="":
            return None
        else:
            return depend_key

    #判断本case中的字段名是否存在
    def is_depend(self,row):
        col = int(data_config.get_field_depend())
        data = self.oper_execl.get_cell_value(row,col)
        if data =='':
            return None
        else:
            return data



    def write_result(self,row,value):
        col = data_config.get_result()
        self.oper_execl.write_value(row,col,value)

