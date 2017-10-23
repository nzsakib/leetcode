
# Write a function to find the longest common prefix string amongst an array of strings. 
# 
class Solution:
    def prefix(self, str1, str2):
        
        string = []
 
        l1 = len(str1)
        l2 = len(str2)
        i = j = 0

        while i < l1 and j < l2:
            if str1[i] != str2[j]:
                break 
            string.append(str1[i])
            i += 1
            j += 1
        
        return str.join('', string)

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs)
        if length == 0:
            return ""
        pre = strs[0]
        for i in range(1, length):
            pre = self.prefix(pre, strs[i])

        return pre 

l = Solution()
print( l.longestCommonPrefix(['geekforgeeks', 'geeks', 'geek']) )
        
