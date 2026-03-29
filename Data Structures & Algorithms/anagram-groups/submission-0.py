class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        res = []

        for s in strs:
            sorted_s = "".join(sorted(s))

            if sorted_s not in mp:
                mp[sorted_s] = len(res)
                res.append([])

            res[mp[sorted_s]].append(s)

        return res

            


        

        