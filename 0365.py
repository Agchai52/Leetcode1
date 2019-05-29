class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        return (z == 0) or (z <= x+y and z % self.gcd(x,y) == 0)
    
    def gcd(self, x, y): # greatest common divisor
        return x if y == 0 else self.gcd(y, x%y)
