class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        i=0
        c=0
        for j in range (len(s)):
            if s[j] not in d or d[s[j]]<i:
                    d[s[j]]= j
                    c=max(c, j-i+1)
                    #print(d)
            else:
                    i=d[s[j]]+1
                    d[s[j]]=j
        return c