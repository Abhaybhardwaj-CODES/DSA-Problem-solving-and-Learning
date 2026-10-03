class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        # If n is odd, all 'a's will have an odd count (n)
        if n % 2 != 0:
            return 'a' * n
        # If n is even, 'a' appears n-1 times (odd) and 'b' appears 1 time (odd)
        else:
            return 'a' * (n - 1) + 'b'
