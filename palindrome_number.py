# Added by branch 2
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative number is not palindrome
        if x < 0:
        	return False

        z = x
        rev = 0

        prev = rev
        while ( z != 0 ):
        	current = z % 10
        	rev = rev * 10 + current
        	if (rev - current) / 10 != prev: # 32 bit integer overflow check
        		return False
        	prev = rev
        	z = int(z / 10)

        if x == rev:
        	return True
        else:
        	return False

l = Solution()
print(l.isPalindrome(-1))

