import socket

def get_pod_ips(service_name, namespace="default"):
    dns_name = f"{service_name}.{namespace}.svc.cluster.local"
    try:
        ip_addresses = socket.gethostbyname_ex(dns_name)[-1]
        return ip_addresses
    except socket.gaierror:
        return []

# 指定 Service 的名称和命名空间
service_name = "gc3a-stable-diffusion-service"
namespace = "g123-data"

# 调用函数获取 IP 地址列表
ip_list = get_pod_ips(service_name, namespace)

# 打印 IP 地址列表
for ip in ip_list:
    print(ip)
