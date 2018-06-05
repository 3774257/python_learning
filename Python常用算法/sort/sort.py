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
    if len(li) <= 1:
        return
    __quick_sort_sub(li, 0, len(li)-1)


def __quick_sort_sub(li, i, j):
    if i >= j:
        return
    t = li[i]
    ii = i
    jj = j
    while i < j:
        while i < j and li[j] > t:
            j -= 1
        li[i] = li[j]
        while i < j and li[i] < t:
            i += 1
        li[j] = li[i]
    li[i] = t
    __quick_sort_sub(li, ii, i-1)
    __quick_sort_sub(li, i+1, jj)


@getfuntime
def tim_sort(li):
    pass


@getfuntime
def heap_sort(li):
    pass


if __name__ == '__main__':
    l = list(range(2000))
    shuffle(l)
    # l = [19, 11, 6, 18, 10, 0, 12, 13, 15, 17, 1, 16, 3, 14, 9, 7, 2, 8, 4, 5]
    print(l)
    quick_sort(l)
    print(l)
    shuffle(l)
    insert_sort(l)
    shuffle(l)
    select_sort(l)
    shuffle(l)
    bubble_sort(l)
    shuffle(l)
    bubble_sort2(l)
