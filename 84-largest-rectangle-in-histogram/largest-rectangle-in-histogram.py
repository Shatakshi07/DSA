class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        leftsmall=[0]*n
        rightsmall=[0]*n
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if not stack:
                leftsmall[i]=0
            else:
                leftsmall[i]=stack[-1]+1
            stack.append(i)

        while stack:
            stack.pop() #clear the stack to be reused
        
        for i in range(n)[::-1]:
            while stack and heights[stack[-1]]>= heights[i]:
                stack.pop()
            if not stack:
                rightsmall[i]=n-1
            else:
                rightsmall[i]=stack[-1]-1
            stack.append(i)
        
        maxA=0
        for i in range(n):
            maxA=max(maxA , heights[i]*(rightsmall[i]-leftsmall[i]+1))
        
        return maxA








    def largestRectangleArea2(self, heights: List[int]) -> int:
        m=min(heights)
        if m!=0:
            mv=max(max(heights),m*len(heights))
        else:
            mv=max(heights)
        area=0
        for i in range(len(heights)):
            c=1
            if heights[i]==m:
                continue
            smallv=heights[i]
            for j in range(i+1,len(heights)):
                if heights[j]==m:
                    break
                else:
                    smallv=min(smallv,heights[j])
                    c+=1
                    area=smallv*c
                    mv=max(mv,area)
           
        return mv