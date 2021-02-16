from typing import List
import self as self

#Running sum of an array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        value = 0
        array = []
        for x in nums:
            value += x
            array.append(value)
        return array

print(Solution.runningSum(self,[1, 2, 3, 4])
