class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n_s = set()
        for n in nums:
            if n in n_s:
                return True
            else:
                n_s.add(n)
        return False