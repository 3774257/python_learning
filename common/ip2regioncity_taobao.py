import requests
import json


def get_ip_area(ip, proxy = None):
    """从taobao获取IP对应的省市信息"""
    try:
        apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip
        # print(apiurl)
        # content = request.urlopen(apiurl).read().decode('utf-8')
        if proxy:
            content = requests.get(apiurl, proxies={'http': proxy})
        else:
            content = requests.get(apiurl)
        # print(content)
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
        print(ex)


if __name__ == '__main__':
    ip = '125.76.245.13'
    data = get_ip_area(ip)
    if data:
        print(data)

