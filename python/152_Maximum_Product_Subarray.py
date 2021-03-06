'''
    Find the contiguous subarray within an array (containing at least one number) which has the largest product.

    For example, given the array [2,3,-2,4],
    the contiguous subarray [2,3] has the largest product = 6.

'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = minvalue = maxvalue = nums[0]
        for x in nums[1:]:
            maxvalue, minvalue = max(x, x * maxvalue, x * minvalue), min(x, x * maxvalue, x * minvalue)
            ans = max(maxvalue, ans)
        return ans
