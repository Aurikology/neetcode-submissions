class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset: #Checks if our array has any duplicates by putting it in hashset
                return True
            hashset.add(n)
        return False

        