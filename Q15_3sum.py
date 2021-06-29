class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        
        # method 1
        # two passes for i and j (the first two numbers), and find the third number from the set which stores the visited j
        for i in range(0, len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            s = set()
            for j in range(i+1, len(nums)):
                x = -(nums[i] + nums[j])
                if x in s:
                    t = [nums[i],nums[j],x]
                    t.sort()
                    if solution and t == solution[-1]:
                        continue
                    else:
                        solution.append(t)
                else:
                    s.add(nums[j])
        return solution
    
    
        '''
        # method 2
        # one pass for the first number. The 2nd and 3rd numbers pass from the opposite side. (nums already sorted)
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low = i+1
            high = len(nums)-1
            while low < high:
                if nums[i] + nums[low] + nums[high] == 0:
                    if low > i+1 and nums[low] == nums[low-1]:
                        low += 1
                        continue
                    solution.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -= 1
                elif nums[i] + nums[low] + nums[high] > 0:
                    high -= 1
                else:
                    low += 1
        
        return solution
        '''        
        
'''
# method 3
    make use of the 2sum problem

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        indices = {}
        nums.sort()
                
        for idx, num in enumerate(nums):
            indices.setdefault(num, []).append(idx)
        
        for i in range(len(nums)):
            indices[nums[i]].remove(i)
            if i == 0 or nums[i] != previous:
                previous = nums[i]
                self.twoSum(indices, -nums[i], solution)
          
        return solution
    
    
    def twoSum(self, indices, target, solution):

        for k, v in indices.items():
            
            if (k < target/2 and target-k in indices and v and indices[target-k]) or (k == target/2 and len(v) >= 2):
                s = [-target, k, target-k]
                s.sort()
                if s not in solution:
                    solution.append(s)
'''
        
