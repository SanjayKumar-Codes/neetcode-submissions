class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for j in strs:
            a = ''.join(sorted(j))
            if a in result:
                result[a].append(j)
            else:
                result[a] = [j]
        return list(result.values())




        