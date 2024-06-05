class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        for s in stones:
            for j in jewels:
                if (s == j):
                    count += 1
        return count 