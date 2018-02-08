#coding=utf-8
from Data.get_Data import GetData
from Unit.OperationExecl import OperationExecl
from Base.run_method import RunMethod
from jsonpath_rw import  jsonpath,parse

class DeppenddentData:
   def __init__(self,case_id):
       self.case_id =case_id
       self.opera_execl = OperationExecl
       self.data  = GetData()

   #通过case_id去获取一行数据
   def get_case_line_data(self):
       rows_data = self.opera_execl.get_row_data(self.case_id)
       return  rows_data

   #执行依赖测试，获取结果
   def run_deppendt(self):
       #找到依赖case_id----->查询到依赖的行----->依赖行的数据------>依赖行执行请求后返回的数据
       run_method = RunMethod()
       row_num = self.opera_execl.get_row_num(self.case_id)
       request_data = self.data.get_data_for_json(row_num)
       header = self.data.is_header(row_num)
       method  = self.data.get_request_way(row_num)
       url = self.data.get_request_url(row_num)
       res = run_method.run_main(method,url,request_data,header)
       return  res

   #根据依赖的key去获取执行依赖测试case的响应，然后返回
   def  get_data_for_key(self,row):
       deppend_data = self.data.get_depend_key(row)
       response_data = self.run_deppendt(self)

       json_exe = parse(deppend_data)
       madle = json_exe.find(response_data)
       return [math.value for math in madle][0]


