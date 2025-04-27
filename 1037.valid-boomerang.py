# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

# A boomerang is a set of three points that are all distinct and not in a straight line.

 

# Example 1:

# Input: points = [[1,1],[2,3],[3,2]]
# Output: true
# Example 2:

# Input: points = [[1,1],[2,2],[3,3]]
# Output: false

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:

        (x1, y1), (x2, y2), (x3, y3) = points

        if len({(x1, y1), (x2, y2), (x3, y3)}) < 3:
            return False

        return (x2 - x1)*(y3 - y1) != (x3 - x1)*(y2 - y1)