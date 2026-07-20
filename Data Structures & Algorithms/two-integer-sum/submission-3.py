class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # setp 1 use target numer to minus one element
        # search for the rest elements which the value equals to the result from step 1
        # if the relsult matches the element then return the index
        # first we can transform this index into dict

        my_dict = dict(enumerate(nums))
        for i in my_dict:
            minus = target - my_dict.get(i)

            for j in my_dict:
                if j == i:
                    continue

                if my_dict[j] == minus:
                    return [i,j]


        
                        
        