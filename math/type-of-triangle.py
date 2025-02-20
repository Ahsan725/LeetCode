class Solution:
    def triangleType(self, nums: List[int]) -> str:
        x, y, z = nums
        if x+y>z and y+z>x and z+x>y:
            if x == y == z:
                return "equilateral"
            elif x == y or y == z or z == x:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"