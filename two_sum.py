class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {value: index for index, value in enumerate(nums)}
        pairs = []


        for i in range(len(nums)):
            rem = target - nums[i]
            f = hm.get(rem)
            if f != None and f != i : 
                pairs.append(f)
                pairs.append(i)
        return(set(pairs))
