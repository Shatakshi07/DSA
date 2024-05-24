class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix[0])
        m=len(matrix)
        nums=[0]*(m*n)
        k=0
        for i in range(m):
            for j in range(n):
                nums[k]=matrix[i][j]
                k+=1
        print(nums)
        left=0
        right=len(nums)-1
        while left<=right:
            mid=int(left+right)//2
            if(nums[mid]==target):
                print(nums[mid])
                return True
            elif(nums[mid]>target):
                right=mid-1
            else:
                left=mid+1
        return False


    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix[0])
        m=len(matrix)
        mid=0
        def bs(i,j)-> int:
            if (i<=j):
                mid=int((i+j))//2
                midI=mid//n
                midJ=mid-(n*midI)
                if midI>=0 and midI<m and midJ>=0 and midJ<n:

                    #print(f"midI: {midI}")
                    #print(f"midJ: {midJ}")
                    #print(f"matrix[midI][midJ]: {matrix[midI][midJ]}")
                    if target==matrix[midI][midJ] :
                        return True
                    elif target<matrix[midI][midJ]:
                        return bs(i,mid-1)
                    else:
                        return bs(mid+1,j)
                else:
                    return False
            else:
                return False
        flag=bs(0,(m*n)-1)
        return flag

            
