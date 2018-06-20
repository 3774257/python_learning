class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closetarget = sum(nums[:3])
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if j + 1 <= n - 1:
                    cha = target - nums[i] - nums[j]
                    closecha = self.binsearch(nums, cha, j + 1, n - 1)
                    if abs(cha - closecha) < abs(target - closetarget):
                        closetarget = nums[i] + nums[j] + closecha
        return closetarget

    def binsearch(self, nums, cha, left, right):
        if left == right:
            return nums[left]

        mid = (left + right) // 2
        while left < mid < right:
            cha1 = abs(cha - nums[mid - 1])
            cha2 = abs(cha - nums[mid])
            cha3 = abs(cha - nums[mid + 1])
            if cha1 == cha2 == cha3:
                mid = mid-1 if abs(cha - left) < abs(cha - right) else mid+1
            if cha1 <= cha2 <= cha3:
                right = mid
            elif cha1 >= cha2 >= cha3:
                left = mid
            else:
                return nums[mid]
            mid = (left + right) // 2
        return nums[left] if abs(cha - left) <= abs(cha - right) else nums[right]


if __name__ == '__main__':
    nums = [-30,29,-27,53,40,36,40,-76,58,64,85,2,56,11,-82,-65,14,-26,-44,-7,80,44,-68,-44,89,-96,93,-37,-75,21,5,-67,12,61,-3,-41,-77,35,-70,35,18,-29,-28,-24,-47,-58,-63,-37,49,99,-99,-68,56,-52,-13,16,-18,-41,78,-82,42,8,-30,-12,9,-98,82,-16,33,96,55,-43,22,52,81,-56,39,26,76,82,82,25,-10,-33,-76,-22,-39,36,-15,94,-87,-17,46,-95,-13,-38,87,-91,37,-6,-51,-9,-59,49,-99,-2,24,43,95,-23,-79,-1,-91,-28,81,6,-95,-19,26,-94,77,-76,-13,69,-22,-14,-18,32,73,-70,61,16,58,76,35,41,-64,-44,67,51,70,56,-46,-97,81,3,-7,30,-87,82,6,100,-4,-47,-89,-26,61,-79,1,-91,40,-57,-79,-79,58,-52,48,-34,-61,-56,77,73,96,-9,93,-11,-59,13,20,-34,-85,-8,-37,-17,-21,-12,-87,67,-2,10,-41,-95,22,-69,65,-53,54,48,35,54,3,-19,-17]
    target = -184
    sl = Solution()
    print(sl.threeSumClosest(nums, target))
