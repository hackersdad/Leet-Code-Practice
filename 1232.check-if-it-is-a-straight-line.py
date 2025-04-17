# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

# Example 1:



# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        def slope(x1,y1,x2,y2):
            y = abs(y2-y1)
            x = abs(x2-x1)
            if x == 0:
                return 90
            else:
                return y/x
        s = slope(coordinates[0][0],coordinates[0][1],coordinates[-1][0],coordinates[-1][1])
        
        x1,y1 = coordinates[0][0],coordinates[0][1]
        i = 1
        while i<len(coordinates):
            x2,y2 = coordinates[i][0],coordinates[i][1]
            new_s =  slope(x1,y1,x2,y2)
            if new_s != s:
                return False
            x1,y1 = coordinates[i][0],coordinates[i][1]
            i += 1
        return True

        