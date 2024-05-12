class Solution:
    def productExceptSelf_TRIAL(self, nums: List[int]) -> List[int]:
        p=[] #prefix products
        s=[] #suffix products
        prefix_prod=1
        suffix_prod=1
        out=[]
        for i in range(len(nums)):
            p.append(nums[i]*p[i-2])
        for i in range(len(nums)-1, -1 ,-1):
            s.append(nums[i]*s[i-2])

        for i in range(len(nums)):
            out.append(p[i]*s[i])
        return out#......incomplete

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1 
        q=1
        out=[]
        for i in range(len(nums)):
            p=p*nums[i]
        for i in range(len(nums)):
            if p!=0:
                out.append(int(p/nums[i]))
            else:
                if nums[i]!=0:
                    out.append(0)
                else:
                    for j in range(len(nums)):
                        if j!=i:
                            q=q*nums[j]
                    out.append(q)
        return out
                