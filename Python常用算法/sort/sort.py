from common.funtiontime import getfuntime
from random import shuffle


@getfuntime
def bubble_sort(li):
    n = len(li)
    for i in range(n - 1):
        for j in range(n-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]


@getfuntime
def bubble_sort2(li):
    n = len(li)
    for i in range(n - 1):
        flag = False
        for j in range(n-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                flag = True
        if not flag:
            break


@getfuntime
def select_sort(li):
    n = len(li)
    for i in range(n-1):
        t = i
        for j in range(i+1, n):
            if li[t] > li[j]:
                t = j
        if i != t:
            li[i], li[t] = li[t], li[i]


@getfuntime
def insert_sort(li):
    n = len(li)
    for i in range(1, n):
        if li[i] >= li[i-1]:
            continue
        for j in range(i, 0, -1):
            if li[j] < li[j-1]:
                li[j - 1], li[j] = li[j], li[j-1]
            else:
                break


@getfuntime
def quick_sort(li):
    pass


@getfuntime
def tim_sort(li):
    pass


@getfuntime
def heap_sort(li):
    pass


if __name__ == '__main__':
    l = list(range(2000))
    shuffle(l)
    insert_sort(l)
    print(l)
    shuffle(l)
    select_sort(l)
    shuffle(l)
    bubble_sort(l)
    shuffle(l)
    bubble_sort2(l)
