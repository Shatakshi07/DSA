class Solution:
    def trap(self, height: List[int]) -> int:
        i=0
        v=0
        j=len(height)-1
        while height[i]==0 and i<j:
            i+=1
        while height[j]==0 and i<j:
            j-=1
        m=height.index(max(height))
        #print (m)
        while i<j:
            k=i+1
            if k>m:
                break
            while height[k]<=height[i]:
                k+=1
            v+=height[i]*(k-i-1)
            s=0
            for n in range(i+1,k):
                if height[n]!=0 :
                     s+=height[n]
            v-=s
            i=k
           

        while i<j:
            l=j-1
            if l<m:
                break
            while height[l]<=height[j] and l>=m:
                l-=1
            v+=height[j]*(j-l-1)
            s=0
            for n in range(l+1,j):
                if height[n]!=0 :
                     s+=height[n]
            v-=s
            j=l
        return v
