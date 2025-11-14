class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows == 1):
            return s
        n = len(s)
        cycleLen = 2 * numRows - 2
        result = ""
        for row in range(0, numRows):
            i = row
            toggle = False
            while(i < n):
                result += s[i]
                i += cycleLen if(row == 0 or row == numRows - 1) else 2 * row if(toggle) else cycleLen - 2 * row
                toggle = not toggle
        return result