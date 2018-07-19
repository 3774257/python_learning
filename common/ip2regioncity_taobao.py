import requests
import json


def get_ip_area(ip, **kwargs):
    """从taobao获取IP对应的省市信息
    ip: ip="192.168.1.1"
    proxies: proxies=proxies = {'http': "202.1.1.1:8888"}
    timeout: timeout=30
    """
    try:
        apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip
        # print(apiurl)
        # content = request.urlopen(apiurl).read().decode('utf-8')

        content = requests.get(apiurl, **kwargs)
        data = json.loads(content.text)['data']
        code = json.loads(content.text)['code']
        if code == 0:
            ret = {}
            ret['ip'] = data['ip']
            ret['country'] = data['country']
            ret['region'] = data['region']
            ret['city'] = data['city']
            return ret
        else:
            print(data)
            return {}
    except Exception as ex:
        pass


if __name__ == '__main__':
    sip = '125.76.245.13'
    from time import time
    t1 = time()
    data = get_ip_area(sip)
    print("Cost Time:", time() - t1)
    if data:
        print(data)

