import socket
from datetime import datetime

def get_current_time_hostname_ip():
    # 获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 获取本机的主机名
    hostname = socket.gethostname()

    # 获取本机的 IP 地址
    ip_address = socket.gethostbyname(hostname)

    # 组合字符串
    result = f"Current Time: {current_time}\nHostname: {hostname}\nIP Address: {ip_address}"

    return result

# 调用函数并打印结果
print(get_current_time_hostname_ip())
