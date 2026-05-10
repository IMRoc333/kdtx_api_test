from config import project_path



import json


#断言status_code和code和msg
def assert_response(response, expected_status_code=200, expected_code=200, expected_msg="成功"):
    assert response.status_code == expected_status_code
    assert response.json()["code"] == expected_code
    assert response.json()["msg"] == expected_msg


def read_json_to_tuples(file_path):
    """读取json文件，将 [{}, {}, {}] 转为 [(), (), ()]"""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [tuple(d.values()) for d in data]

if __name__ == '__main__':
    print(read_json_to_tuples(f"{project_path}/data/login.json"))
