from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ar=[]
        for i in range(n):
            ar.append(nums[i])
            ar.append(nums[n+i])
        return ar

nums = [2, 5, 1, 3, 4, 7]
n = 3
s = Solution()
print(s.shuffle(nums,n))


