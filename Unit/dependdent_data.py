#coding:utf-8
import json

from Data.get_Data import GetData
from Unit.OperationExecl import OperationExecl
from Base.run_method import RunMethod
from jsonpath_rw import jsonpath,parse

class DeppenddentData:

   def __init__(self,case_id):
       self.case_id =case_id
       self.opera_execl = OperationExecl()
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
       #header = self.data.is_header(row_num)
       method  = self.data.get_request_way(row_num)
       url = self.data.get_request_url(row_num)
       res = run_method.run_main(method,url,request_data)
       return  json.loads(res)

   #根据依赖的key去获取执行依赖测试case的响应，然后返回
   def  get_data_for_key(self,row):
       deppend_data = self.data.get_response_data_depend(row)
     #  deppend_data =deppend_data.encode('unicode-escape').decode('string_escape')
       response_data = self.run_deppendt()
       print deppend_data
       print type(deppend_data)
       print  type(response_data)
       print  response_data
       json_exe = parse(deppend_data)
       madle = json_exe.find(response_data)
       return [math.value for math in madle][0]


if __name__=='__main__':
    order = {
        "data": {"_input_charset": "utf-8", "body": "\u6155\u8bfe\u7f51\u8ba2\u5355-1802162130507528",
                 "extra_common_param": "1802162130507528", "it_b_pay": "1d",
                 "notify_url": "http:\/\/order.imooc.com\/pay\/notifyalipay",
                 "out_trade_no": "1802162130503193329686", "partner": "2088821622341845", "payment_type": "1",
                 "seller_id": "13911155184@139.com", "service": "mobile.securitypay.pay",
                 "subject": "\u6155\u8bfe\u7f51\u8ba2\u5355-1802162130507528", "total_fee": "299.00",
                 "sign": "G4ldiAFhXiffrHL58nKfMOB4Ua9ofL4kgpF%2BUG5PbT53i4F%2FnpipGXcl0k00SRoGz6RxtcHijQtMAVzqeDf6dlK4%2FuT0iXDYocniG6sEe1ODk4HhngzOv6hiN8%2Bi%2FaodGvun0UoipsaqlxFKElJu%2BR1meiq9zcyUFpxIyxrYlCE%3D",
                 "sign_type": "RSA",
                 "string": "_input_charset=utf-8&body=\u6155\u8bfe\u7f51\u8ba2\u5355-1802162130507528&extra_common_param=1802162130507528&it_b_pay=1d&notify_url=http:\/\/order.imooc.com\/pay\/notifyalipay&out_trade_no=1802162130503193329686&partner=2088821622341845&payment_type=1&seller_id=13911155184@139.com&service=mobile.securitypay.pay&subject=\u6155\u8bfe\u7f51\u8ba2\u5355-1802162130507528&total_fee=299.00&sign=G4ldiAFhXiffrHL58nKfMOB4Ua9ofL4kgpF%2BUG5PbT53i4F%2FnpipGXcl0k00SRoGz6RxtcHijQtMAVzqeDf6dlK4%2FuT0iXDYocniG6sEe1ODk4HhngzOv6hiN8%2Bi%2FaodGvun0UoipsaqlxFKElJu%2BR1meiq9zcyUFpxIyxrYlCE%3D&sign_type=RSA"
                 }

    }
    res = 'data.out_trade_no'
    print type(res)
    print type(order)
    json_exe = parse(res)
    madle = json_exe.find(order)
    print [math.value for math in madle][0]
