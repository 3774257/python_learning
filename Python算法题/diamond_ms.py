"""
一楼到十楼的每层电梯门口都放着一颗钻石，钻石大小不一。
你乘坐电梯从一楼到十楼，每层楼电梯门都会打开一次，只能拿一次钻石，
问怎样才能拿到最大的一颗？
"""
from random import shuffle


def main():
    MAXCOUNT = 10000
    N = 10
    diamonds = list(range(1, N + 1))
    for k in range(0, N):
        results = []
        for _ in range(MAXCOUNT):
            shuffle(diamonds)
            if diamonds[:k]:
                curmax = max(diamonds[:k])
            else:
                curmax = 0
            for i in range(k, N):
                if diamonds[i] > curmax:
                    curmax = diamonds[i]
                    break
            else:
                curmax = diamonds[-1]
            results.append(curmax)
        print('跳过%d层后选更大值，结果平均值%.2f 最大值比例%.2f%%' % (k, sum(results) / MAXCOUNT, len(list(filter(lambda x: x == N, results)))/MAXCOUNT*100))


if __name__ == '__main__':
    main()
