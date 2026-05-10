import requests 
from config import base_url


class LoginApi:
    #获取验证码
    def get_code(self):
        return requests.get(base_url + "/api/captchaImage")
    
    #登录接口
    def login(self, login_data):
        return requests.post(base_url + "/api/login", json=login_data)
