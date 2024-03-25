class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        p1 = 0
        p2 = fast
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1
