class Solution:
    def isPalindrome(self, s: str) -> bool:
        # transcform all capital into regular c
        # remove all numbers
        # remove all symbols and spaces
        # just keep the lower characters

        newstr = ""

        for c in s:
            if c.isalnum() == True:
                newstr += c.lower()

        

        return newstr == newstr[::-1]




        