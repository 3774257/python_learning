from urllib import request
import json

"""从taobao获取IP对应的省市信息"""
def get_ip_area(ip):
    try:
        apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip
        print(apiurl)
        content = request.urlopen(apiurl).read().decode('utf-8')
        print(content)
        data = json.loads(content)['data']
        code = json.loads(content)['code']
        if code == 0:
            print("ip=", data['ip'])
            print("country=", data['country'])
            print("area=", data['area'])
            print("region=", data['region'])
            print("city=", data['city'])
            print("isp=", data['isp'])
            print("country_id=", data['country_id'])
            print("area_id=", data['area_id'])
            print("region_id=", data['region_id'])
            print("city_id=", data['city_id'])
        else:
            print(data)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    ip = '125.76.245.13'
    get_ip_area(ip)
