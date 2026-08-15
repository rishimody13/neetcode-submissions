class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for i in strs:
            ans+=(i+"~")
        return ans
    def decode(self, s: str) -> List[str]:
        ans = s.split("~")
        a = ans.pop()
        return ans