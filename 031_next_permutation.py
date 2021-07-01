class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        
        # find the first decreasing number from back to front
        have_next = True
        
        x = len(nums) - 1
        while x >= 1:
            if nums[x] <= nums[x-1]:
                if x == 1:
                    have_next = False
                    x = -1
                    break
                x -= 1
            else:
                x -= 1
                break
        
        if have_next:
            # find the number just larger than x
            min = math.inf
            idx = -1
            for i in range(x + 1, len(nums)):
                if nums[i] - nums[x] > 0 and nums[i] - nums[x] <= min:
                    min = nums[i] - nums[x]
                    idx = i

            self.swap(nums, x, idx)

        # reverse the elements from the end
        for i in range(x + 1, int((x + len(nums))/2)+1):
            self.swap(nums, i, x + len(nums) - i)
        
                
    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp
