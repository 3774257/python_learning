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
    n = len(li)
    pos = [0]
    for i in range(1, n):
        if li[i] < li[i-1]:
            pos.append(i)
    pos.append(n)
    while len(pos) > 2:
        for i in range(len(pos)-3, -1, -2):
            t1 = pos[i]
            t2 = pos[i+1]
            # right = pos[i+2]
            tl = []
            while t1 < pos[i+1] and t2 < pos[i+2]:
                if li[t1] <= li[t2]:
                    tl.append(li[t1])
                    t1 += 1
                else:
                    tl.append(li[t2])
                    t2 += 1
            if t1 < pos[i+1]:
                tl.extend(li[t1:pos[i+1]])
            else:
                tl.extend(li[t2:pos[i + 2]])
            li[pos[i]:pos[i+2]] = tl
            del pos[i+1]


@getfuntime
def heap_sort(li):
    n = len(li)
    for i in range(n//2-1, -1, -1):
        __heap_shift(li, i, n-1)
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        __heap_shift(li, 0, i-1)


def __heap_shift(li, i, j):
    sub = 2*i + 1
    t = li[i]
    while sub <= j:
        if sub < j and li[sub] < li[sub+1]:
            sub += 1
        if t < li[sub]:
            li[i] = li[sub]
            i = sub
            sub = 2*i+1
        else:
            break
    li[i] = t


@getfuntime
def merge_sort(li):
    __merge_sort_sub(li, 0, len(li)-1)


def __merge_sort_sub(li, i, j):
    if i >= j:
        return
    mid = (i+j)//2
    __merge_sort_sub(li, i, mid)
    __merge_sort_sub(li, mid+1, j)
    tl = []
    ti, tj = i, mid + 1
    while ti <= mid and tj <= j:
        if li[ti] < li[tj]:
            tl.append(li[ti])
            ti += 1
        else:
            tl.append(li[tj])
            tj += 1
    if ti <= mid:
        tl.extend(li[ti:mid+1])
    else:
        tl.extend(li[tj:j+1])
    li[i:j+1] = tl[:]


@getfuntime
def sys_sort(li):
    li.sort()


if __name__ == '__main__':
    l = list(range(2000))
    # l = [19, 11, 6, 18, 10, 0, 12, 13, 15, 17, 1, 16, 3, 14, 9, 7, 2, 8, 4, 5]
    shuffle(l)
    sys_sort(l)
    shuffle(l)
    tim_sort(l)
    shuffle(l)
    heap_sort(l)
    shuffle(l)
    merge_sort(l)
    shuffle(l)
    quick_sort(l)
    shuffle(l)
    insert_sort(l)
    shuffle(l)
    select_sort(l)
    shuffle(l)
    bubble_sort(l)
    shuffle(l)
    bubble_sort2(l)
