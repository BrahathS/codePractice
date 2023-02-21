class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict: Dict[int, int] = {}
        for i, num in enumerate(nums):
            # if target - num in num_dict, we've found a match
            # Return the indices of the match and the current index
            if target - num in num_dict:
                return [num_dict[target - num], i]
            # If no match, add the current number to the dictionary
            # with the index as the value
            num_dict[num] = i
        # If no match is found, return an empty list
        return []
