import requests
from config import base_url

#封装课程类
class CourseApi:
    #新增课程
    def add_course(self,token,course_data):
        return requests.post(base_url + "/api/clues/course",
                              headers={"Authorization": token},
                              json=course_data)
    
    #查询课程列表
    def get_course_list(self,token,query_data):
        return requests.get(base_url + "/api/clues/course/list",
                            headers={"Authorization": token},
                            params=query_data)
    
    #查询课程
    def get_course(self,token,course_id): 
        return requests.get(base_url + "/api/clues/course/:id" ,
                            headers={"Authorization": token},
                            params={"courseId": course_id})
    #修改课程
    def update_course(self,token,course_data):
        return requests.put(base_url + "/api/clues/course",
                            headers={"Authorization": token},
                            json=course_data)
    
    #删除课程
    def delete_course(self,token,course_id):
        return requests.delete(base_url + "/api/clues/course/:id",
                              headers={"Authorization": token},
                              params={"courseId": course_id})
