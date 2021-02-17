from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ar=[]
        for i in accounts:
            ar.append(sum(i))
        return max(ar)

accounts = [[1, 2, 3], [3, 2, 1]]
s = Solution()
print(s.maximumWealth(accounts))
