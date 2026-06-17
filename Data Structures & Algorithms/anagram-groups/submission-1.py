from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        
        dic = {}

        for i, s in enumerate(strs):
            sort_s = "".join(sorted(s))
            if sort_s not in dic:
                dic[sort_s] = set([i])

            else:
                dic[sort_s].add(i)

        for sorted_s in dic:
            new_group = []
            for j in dic[sorted_s]:
                new_group.append(strs[j])
            final.append(new_group)

        return final

            
            