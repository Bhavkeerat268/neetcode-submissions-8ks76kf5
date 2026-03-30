class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [1] * len(nums)
        suffix_array = [1] * len(nums)

        for i in range(len(nums)-1):
            prefix_array[i+1] = prefix_array[i]*nums[i]

        for j in range(len(nums)-1, 0, -1):
            suffix_array[j-1] = suffix_array[j]*nums[j]

        for i in range(len(nums)):
            nums[i] = prefix_array[i] * suffix_array[i]

        return nums
