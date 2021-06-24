# Two sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for idx, num in enumerate(nums):
            indices.setdefault(num, []).append(idx)
        print(indices.items())
        for k, v in indices.items():
            i = v.pop()
            if target - k in indices and indices[target-k]:
                return i, indices[target-k].pop()
