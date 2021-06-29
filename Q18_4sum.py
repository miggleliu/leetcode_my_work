class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        solution = []
        
        # 
        for w in range(len(nums)-3):
            if w > 0 and nums[w] == nums[w-1]:
                continue
            for x in range(w+1, len(nums)-2):
                if x > w+1 and nums[x] == nums[x-1]:
                    continue  
                y = x + 1
                z = len(nums) - 1
                while y < z:
                    sum = nums[w] + nums[x] + nums[y] + nums[z]
                    if sum == target:
                        if y > x+1 and nums[y] == nums[y-1]:
                            y += 1
                            continue
                        solution.append([nums[w], nums[x], nums[y], nums[z]])
                        y += 1
                        z -= 1
                    elif sum > target:
                        z -= 1
                    else:
                        y += 1
        return solution
