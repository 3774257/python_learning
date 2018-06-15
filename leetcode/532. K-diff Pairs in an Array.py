class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        if k < 0:
            return 0
        n = len(nums)
        cnts = 0
        left = 1
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            he = k + nums[i]
            if he < nums[i]:
                break
            left = max(left, i+1)
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == he:
                    cnts += 1
                    break
                if nums[mid] > he:
                    right = mid - 1
                else:
                    left = mid + 1

        return cnts

    def findPairs2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        if k < 0:
            return 0
        n = len(nums)
        cnts = 0
        left = 1
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            he = k + nums[i]
            left = max(left, i+1)
            while left < n-1 and nums[left] < he:
                left += 1
            if nums[left] == he:
                cnts += 1
        return cnts

    def findPairs3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0 or len(nums) < 2:
            return 0
        nums.sort()
        n = len(nums)
        cnts = 0
        i, j = 0, 1
        while i < n and j < n:
            if nums[j] - nums[i] == k:
                i += 1
                j += 1
                cnts += 1
                while i < n and nums[i] == nums[i - 1]:
                    i += 1
                if i >= j:
                    j = i + 1
            elif nums[j] - nums[i] < k:
                j += 1
            else:
                i += 1
                while i < n and nums[i] == nums[i - 1]:
                    i += 1
                if i >= j:
                    j += 1
        return cnts


if __name__ == '__main__':
    sl = Solution()
    nums = [1,2,3,1,4]
    k = 0

    print(sl.findPairs2(nums, k))