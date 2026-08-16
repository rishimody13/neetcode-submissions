class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        ans = ""
        length = min(len(word1), len(word2))
        while i<length:
            ans+=word1[i]
            ans+=word2[i]
            i+=1
        if len(word1)>len(word2):
            ans+=word1[i:len(word1)]
            return ans
        elif len(word2)>len(word1):
            ans+=word2[i:len(word2)]
            return ans
        else:
            return ans