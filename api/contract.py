import requests 
from config import base_url


#封装合同模块
class ContractApi:
    #合同上传
    def upload_contract(self,token,file_path):
        return requests.post(base_url + "/api/common/upload",
                              headers={"Authorization": token},
                              files={"file": open(file_path, "rb")})

    #新增合同
    def add_contract(self,token,contract_data):
        return requests.post(base_url + "/api/contract",
                              headers={"Authorization": token},
                              json=contract_data)
    
    #查询合同列表
    def get_contract_list(self,token,phone):
        return requests.get(base_url + "/api/contract",
                            headers={"Authorization": token},
                            params={"phone": phone})
    
    #删除合同
    def delete_contract(self,token,contract_id):
        return requests.post(base_url + "/api/contract/remove/",
                              headers={"Authorization": token},
                              params={"contractId": contract_id})
