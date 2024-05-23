class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]
        stack = []
        
        for p, s in sorted(cars)[::-1]:
            time_taken = (target - p) / s
            if not stack or time_taken > stack[-1]:
                stack.append(time_taken)
        
        return len(stack)
        
    def carFleet2(self, target: int, position: List[int], speed: List[int]) -> int:
        adn=[0]*len(speed)
        m=min(speed)
        for i in range(len(speed)):
            adn[i]=position[i]+speed[i]
        #adn.sort()
        print(adn)
        c=1
        i=0
        while max(speed)>m:
            for i in range(len(adn)):
                while i<len(adn)-1 and adn[i]==adn[i+1]:
                    if speed[i]< speed[i+1]:
                        speed[i+1]=speed[i]
                    else:
                        speed[i]=speed[i+1]
                    i+=1

            for i in range(len(speed)):
                adn[i]=position[i]+speed[i]  

            unique_elements = set(adn)
            c=len(unique_elements)     
            
        return c

        
