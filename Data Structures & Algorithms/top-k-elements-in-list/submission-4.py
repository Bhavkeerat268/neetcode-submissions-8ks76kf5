class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_array = {}
        frequency_bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num not in frequency_array:
                frequency_array[num] = 0

            frequency_array[num]+=1

        for num, value in frequency_array.items():
            frequency_bucket[value].append(num)

        output = []
        for i in range(len(frequency_bucket) - 1, -1, -1):
            for item in frequency_bucket[i]:
                output.append(item)
                if len(output) == k:
                    return output





        



            
        