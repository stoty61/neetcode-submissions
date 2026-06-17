from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for string in strs:
            word = "".join(sorted(string))
            if word in words:
                words[word].append(string)
            else:
                words[word] = [string]

        return words.values()


        