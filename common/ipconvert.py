def inet_iton(strip):
    if not isinstance(strip, str):
        raise ValueError("非法IP地址：%s" % strip)
    ns = list(filter(lambda x: 0 <= x <= 255, map(int, strip.split('.'))))
    if len(ns) != 4:
        raise ValueError("非法IP地址：%s" % strip)

    n = 0
    for xx in ns:
        n = n*256 + xx
    return n


def inet_ntoi(nip):
    if isinstance(nip, int) and not 0 <= nip < 256**4:
        raise ValueError("非法IP地址值：%d" % nip)
    return '.'.join([str((nip >> (8*i)) % 256) for i in range(3, -1, -1)])


if __name__ == '__main__':
    ip = '7.91.205.21'
    print(inet_iton(ip), inet_ntoi(4078174207))
