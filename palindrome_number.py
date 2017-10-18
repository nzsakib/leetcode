
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        flag = 0 # indicate negative number 
        if x < 0:
        	return False
        	flag = 1
        	x = x * -1

        z = x
        rev = 0
        # print(z)
        prev = rev
        while ( z != 0 ):
        	current = z % 10
        	# print(z)
        	rev = rev * 10 + current
        	if (rev - current) / 10 != prev:
        		return False 
        	prev = rev
        	z = int(z / 10)

        if flag == 1:
        	rev = -rev
        	x = -x
        # print(x)
        if x == rev:
        	return True 
        else:
        	return False

l = Solution()
print(l.isPalindrome(-1))

