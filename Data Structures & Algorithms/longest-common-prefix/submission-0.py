class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        counter = 0
        out = ""
        strs.sort()
        word = strs[0]
        while True:
            if counter>=len(word):
                break
            char = word[counter]
            for i in strs:
                if counter >= len(i):
                    return out
                if i[counter]!=char:
                    return out
            out+=char 
            counter+=1
        return out 