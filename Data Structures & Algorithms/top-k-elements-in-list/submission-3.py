class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: frequency dictionary
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: sort based on frequency desc
        nums.sort(key=lambda x: -freq[x])

        result = []
        seen = set()

        # Step 3: iterate and pick unique values in sorted order
        for num in nums:
            if num not in seen:
                result.append(num)
                seen.add(num)

                if len(result) == k:
                    break
        
        return result
