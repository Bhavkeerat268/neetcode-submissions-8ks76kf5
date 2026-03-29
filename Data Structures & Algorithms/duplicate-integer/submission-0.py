class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            elif num in counter:
                return True

        return False

