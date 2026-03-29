class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_array = {}

        for i, ele in enumerate(nums):
            if ele not in count_array:
                count_array[ele] = 0

            count_array[ele]+=1

            if count_array[ele] > 1:
                return True

        return False




        