class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1] * len(nums)
        suffix_prod = [1] * len(nums)
        n =len(nums)

        for i in range(1, n):
            prefix_prod[i] = nums[i-1] * prefix_prod[i-1]
            print(prefix_prod)

        for j in range(n-2, -1, -1):
            suffix_prod[j] = nums[j+1] * suffix_prod[j+1]

        # print(suffix_prod, prefix_prod)

        for t in range(0, len(nums)):
            nums[t] = prefix_prod[t] * suffix_prod[t]

        return nums

        