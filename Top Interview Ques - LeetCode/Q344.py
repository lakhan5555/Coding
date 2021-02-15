class Solution:
    def reverseString(self, s: List[str]) -> None:
        if not s:
            return s
        f = 0
        l = len(s)-1
        while f < l:
            s[f],s[l] = s[l],s[f]
            f += 1
            l -= 1
