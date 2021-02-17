class Solution:
    def defangIPaddr(self, address: str) -> str:
        test= address.replace('.', '[.]')
        return test

s = Solution()
print(s.defangIPaddr("1.1.1.1"))
