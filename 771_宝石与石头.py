class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
      
        j = str(J)
        s = str(S)
        num = 0
        for i in range(0,len(j)):
            num = num + s.count(j[i])
        return num