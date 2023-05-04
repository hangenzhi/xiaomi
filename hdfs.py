from hdfs.client import Client
# 创建连接
client = Client("http://192.168.10.32:9870/", root="/", timeout=900, session=None)
# 创建目录，赋予权限
client.makedirs('/test/01', permission=775)
