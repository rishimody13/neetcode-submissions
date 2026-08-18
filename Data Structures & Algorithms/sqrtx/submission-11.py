class Solution:
    def mySqrt(self, x: int) -> int:
        below = True
        if x == 1 or x==2 or x==3:
            return 1
        for i in range((x)+1):
            if (i*i == x):
                return i
            if (i*i < x):
                below = True
            if (i*i > x) and (below):
                return i-1
        return 0