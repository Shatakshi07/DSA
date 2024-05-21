class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" : return ""

        countT, window = {} , {}
        for c in t:
            countT[c]=1+countT.get(c,0)

        have , need =0 , len(countT)
        res , reslen = [-1,-1] ,float("infinity")
        l=0
        r=0
        for r in range(len(s)):
            c=s[r]
            window[c]= 1+window.get(c ,0)
            if c in countT and window[c]== countT[c]:
                have+=1

            while have == need:
                if reslen>(r-l+1):
                    reslen= r-l+1
                    print(reslen)
                    res= [l,r]
                    print(res)
                c=s[l]
                window[c]-=1
                if c in countT and window[c]< countT[c]:
                    have-=1
                l+=1
        
        l,r=res
        return s[l:r+1] if reslen !=float("infinity") else ""
