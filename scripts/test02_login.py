
#封装登录测试类
from api.login import LoginApi
from tools import assert_response
import pytest
from tools import *



class TestLogin:
    #前置处理
    def setup_method(self):
        #实例化登录接口类
        self.login_api = LoginApi()
        self.response = self.login_api.get_code()
        assert_response(self.response)
    
    #登录
    @pytest.mark.parametrize("username, password, code, status, code2, msg",read_json_to_tuples(f"{project_path}/data/login.json"))
    def test_login(self,username,password,code,status,code2,msg):
        login_data = {
            "username": username,
            "password": password,
            "code": code,
            "uuid": self.response.json().get("uuid")
        }
        response= self.login_api.login(login_data)
        print(response.json())
        assert_response(response,status,code2,msg)
