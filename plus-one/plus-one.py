class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        list_string = map(str, digits)
        d=''.join(list_string)
        d=int(d)+1
        d=list(str(d))
        return map(int,d)
        