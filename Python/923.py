class Solution:
    def threeSumMulti(self, nums: List[int], target: int) -> int:
        nums.sort()
        i = 0
        mod = 1000000007
        sol = 0
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            ctr= 0
            while l < r:
                if nums[i]+nums[l]+nums[r] == target:
                    prevl = nums[l]
                    lctr = 0
                    while l<=r and  nums[l] == prevl:
                        l+=1
                        lctr+=1
                    prevr = nums[r]
                    rctr = 0
                    while l<=r and  nums[r] == prevr:
                        r-=1
                        rctr+=1
                    if prevr != prevl:
                        ctr += (lctr*rctr)%mod
                    else:
                        ctr+= (lctr * (lctr-1))//2
                elif nums[i]+nums[l]+nums[r] < target:
                    l+=1
                else:
                    r-=1
            sol = (sol + ctr)%mod
        return sol
