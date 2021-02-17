class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #check if stones.charat(i)
        #is in jewels
        count=0

        for stonesLetter in stones:
            if stonesLetter in jewels:
                count+=1

        return count


jewels = "aA"
stones = "aAAbbbb"
s= Solution()
print(s.numJewelsInStones(jewels,stones))


