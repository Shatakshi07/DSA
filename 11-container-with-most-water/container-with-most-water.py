class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        mv=0
        while i<j:
            if(height[i]<=height[j]):
                v=height[i]*(j-i)
                i+=1       
            else:
                v=height[j]*(j-i)
                j-=1
           
            if v>mv:
                    mv=v
        return mv
                
                 
