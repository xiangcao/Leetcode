class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        if not rectangles or not rectangles[0]:
            return False

        x1, y1 = float("inf"), float("inf")
        x2, y2 = float("-inf"), float("-inf")
        
        pointSet = set()
        area = 0;
        
        for rect in rectangles:
            x1 = min(rect[0], x1)
            y1 = min(rect[1], y1)
            x2 = max(rect[2], x2)
            y2 = max(rect[3], y2)
            
            area += (rect[2] - rect[0]) * (rect[3] - rect[1])
            
            s1 = str(rect[0]) + " " + str(rect[1])
            s2 = str(rect[0]) + " " + str(rect[3])
            s3 = str(rect[2]) + " " + str(rect[1])
            s4 = str(rect[2]) + " " + str(rect[3])

            for s in [s1, s2, s3, s4]:
                pointSet.remove(s) if s in pointSet else pointSet.add(s) 
        
        if len(pointSet) != 4 or not (str(x1) + " "+ str(y1) in pointSet and str(x1)+ " " + str(y2) in pointSet and str(x2) + " " + str(y1) in pointSet and str(x2) + " " + str(y2) in pointSet):
            return False
        
        return area == (x2-x1) * (y2-y1)
