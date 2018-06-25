# -*- coding: utf-8 -*-
import hashlib
def get_md5(url):
    # 判断URL是否为Unicode编码，将其转换为utf-8格式，不然无法将其加密唯一
    if isinstance(url,str):
        url =url.encode("utf-8")
    #     创建md5对象
    m = hashlib.md5(url)
    # 跟新加密字符串
    m.update(url)
    # 返回获得的加密字符
    return m.hexdigest()
if __name__ == "__main__":
    print(get_md5("http://jobbole.com"))