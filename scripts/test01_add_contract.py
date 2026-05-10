from tools import *
#添加合同测试类
from api.contract import ContractApi
from api.course import CourseApi
from api.login import LoginApi
from config import project_path
import random




class TestAddContract:
    course_id = None
    fileName=None
    #前置处理
    def setup_class(self):
        #实例化登录接口类
        self.login_api = LoginApi()
        #实例化课程接口类
        self.course_api = CourseApi()
        #实例化合同接口类
        self.contract_api = ContractApi()
        #获取验证码
        response= self.login_api.get_code()
        assert_response(response)
        #登录
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": response.json().get("uuid")
        }
        response= self.login_api.login(login_data)
        print(response.json())
        assert_response(response)
        #获取token
        self.token = response.json()["token"]

    
    #新增课程
    def test_add_course(self):
        course_data = {
            "name": "测试课程",
            "price": 100,
            "type": 1,
            "status": 1,
            "description": "测试课程"
        }
        response= self.course_api.add_course(self.token,course_data)
        print(response.json())
        assert_response(response)

    #查询课程
    def test_get_course(self):
        response = self.course_api.get_course_list(self.token, query_data={"name": "jack1015-001-测试开发提升课01"})
        print(response.json())
        assert_response(response)
        TestAddContract.course_id = response.json().get("rows")[0].get("id")

    #上传合同
    def test_upload_contract(self):
        response= self.contract_api.upload_contract(self.token,f"{project_path}/data/testfile.pdf")
        print(response.json())
        assert_response(response)
        TestAddContract.fileName = response.json()["fileName"]

    #新增合同
    def test_add_contract(self):
        contract_data = {
            "name": "测试888",
            "phone": "13610151888",
            # "contractNo": "HT10153212004",
            "contractNo": f"HT101532{random.randint(100000,999999)}",
            "subject": "6",
            "courseId": TestAddContract.course_id,
            "channel": "0",
            "activityId": 77,
            "fileName": TestAddContract.fileName
        }
        response= self.contract_api.add_contract(self.token,contract_data)
        print(response.json())
        assert_response(response)

    #查询合同列表成功
    def test_get_contract_list(self):
        response= self.contract_api.get_contract_list(self.token,phone="13610151888")
        print(response.json())
        assert_response(response)
    