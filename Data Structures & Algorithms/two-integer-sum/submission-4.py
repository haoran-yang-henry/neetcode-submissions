class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # setp 1 use target numer to minus one element
        # search for the rest elements which the value equals to the result from step 1
        # if the relsult matches the element then return the index
        # first we can transform this index into dict

        my_dict = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in my_dict:
                return[my_dict[diff], i]

            my_dict[n] = i
        


        
                        
        