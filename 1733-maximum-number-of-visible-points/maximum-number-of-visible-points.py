class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:

        def get_angles(cd):
            alpha =  math.atan2(cd[0]-location[0] , cd[1]-location[1])  / (math.pi) *180

            if alpha < 0:
                alpha += 360
            
            return alpha

        ans=same=0
        angles=[]
        queue = deque()

        for p in points:
            if p == location :
                same+=1
            else:
                angles.append(get_angles(p))

        angles.sort()

        for a in angles:
            queue.append(a)
            while a - queue[0] > angle:
                queue.popleft()
            
            ans = max(ans, len(queue))

        for a in angles:
            a+=360
            queue.append(a)
            while a - queue[0] > angle:
                queue.popleft()
            
            ans = max(ans, len(queue))

        return ans+same

            