class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n = len(temperatures)
        out = [0] * n  # Initialize the out list with zeros
        stack.append(0)
        for i in range(1,len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx=stack.pop()
                out[idx]= i-idx
            stack.append(i)
        return out
        
            

                
