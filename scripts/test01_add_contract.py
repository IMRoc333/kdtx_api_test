

#添加合同测试类
from api.login import LoginApi


class TestAddContract:
    #前置处理
    def setup_class(self):\
    #实例化登录接口类
    self.login_api = LoginApi()
    
