class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = cnt = 0
        n = len(nums)
        c = None
        for j in range(n):
            if c != nums[j]:
                if i:
                    nums[j - i] = nums[j]
                c, cnt = nums[j], 1
            else:
                if cnt < 2:
                    cnt += 1
                    if i:
                        nums[j - i] = nums[j]
                else:
                    i += 1

        return n - i


if __name__ == '__main__':
    sl = Solution()
    li = [1,1,1,2,2,3]
    ret = sl.removeDuplicates(li)
    print(ret, li[:ret])