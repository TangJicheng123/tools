import requests

url = "https://example.com/api/endpoint"

headers = {
    "Content-Type": "application/json",  # 自定义头部参数
    "Authorization": "Bearer <token>"     # 添加授权头部参数
}

data = {
    "key1": "value1",
    "key2": "value2"
}

params = {
    "param1": "value1",
    "param2": "value2"
}

response = requests.post(url, headers=headers, json=data, params=params)

# 检查请求是否成功
if response.status_code == 200:
    print("请求成功")
    print(response.json())  # 输出JSON格式的响应数据
else:
    print("请求失败")
    print(response.text)  # 打印错误信息
