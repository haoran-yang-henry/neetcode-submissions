class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use hashmap to solve the problem, first craete a default hashmap
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # create a list to store the character frequency
            for c in s:
                count[ord(c) - ord('a')] +=1

            res[tuple(count)].append(s)

        return list(res.values())
                