class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        maxC = max(candies)
        for i in range(len(candies)):
            if (candies[i] + extraCandies >= maxC):
                result.append(True)
            else:
                result.append(False)
            

        return result
        