class Solution:
    def decodeString(self, s: str) -> str:

        def dfs(i):
            ans = ""
            num = 0

            while i < len(s) and s[i] != "]":

                if s[i].isdigit():
                    num = num * 10 + int(s[i])

                elif s[i] == "[":
                  
                    nested, i = dfs(i + 1)
                    ans += num * nested
                    num = 0

                else:
                    ans += s[i]

                i += 1

            return ans, i

        ans, _ = dfs(0)
        return ans