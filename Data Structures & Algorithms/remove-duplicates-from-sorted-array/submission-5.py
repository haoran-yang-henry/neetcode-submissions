class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        num = []
        num.append(nums[0])

        for r in range(1, len(nums)):
            if nums[r-1] != nums[r]:

                nums[l] = nums[r]
                num.append(nums[r])

                l +=1

        print(num)

        return l