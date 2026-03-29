class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            print(diff, seen)
            if diff in seen:
                return [seen[diff], i]

            seen[num] = i
            print("Seen", seen)

        return [-1, -1]



        