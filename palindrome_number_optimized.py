
# Check if a integer is palindrome or not without using extra space 
# Means you cannot create new copy of the given number 

class Solution:
	def isPalindrome(self, x):
		# first find the leading digit
		divisor = 1
		while x / divisor >= 10:
			divisor *= 10
		
		while x != 0:
			lead = int(x / divisor)
			last = x % 10
			# print("lead %d \n last %d" %(lead, last))
			# print(type(lead))
			if lead != last:
				return False 

			# discard leading and last digit 
			x = int((x % divisor) / 10)
			# reduce divisor by two 0's 
			divisor = int(divisor / 100)

		return True

l = Solution()
print(l.isPalindrome(10100101))
