# 算法题，输入两个整数n和sum，从数列1，2，3.......n 中随意取几个数，使其和等于sum，要求将其中所有的可能组合列出来。

n = 20
k = 31


def main(i0=0, i=0, stack=[]):
    while i0 < n:
        # 如果栈为空，插入开始
        if not stack:
            i0 += 1
            i = i0
            if i0 <= n:
                stack.append(i)
                main(i0, i)
                stack.pop()

        else:
            i += 1
            if k - sum(stack) > 2*i + 1 and i < n:
                stack.append(i)
                main(i0, i)
                del stack[-1]
            elif i < k - sum(stack) < n:
                i = k - sum(stack)
                stack.append(i)
                print(stack)
                del stack[-1]
                break
            elif k - sum(stack) == i <= n:
                stack.append(i)
                print(stack)
                del stack[-1]
                break
            else:
                return


if __name__ == '__main__':
    main()
