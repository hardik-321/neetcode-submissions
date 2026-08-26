class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in strs:
            original = i
            i = list(i)
            i.sort()
            i = "".join(i)

            if i not in group:
                group[i] = []
            
            group[i].append(original)
        
        return list(group.values())