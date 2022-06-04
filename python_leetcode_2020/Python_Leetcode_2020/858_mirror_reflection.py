"""
There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)
"""

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        from fractions import Fraction as F

        x = y = 0
        rx, ry = p, q
        targets = [(p, 0), (p, p), (0, p)]

        while (x, y) not in targets:
            #Want smallest t so that some x + rx * t, y + ry * t is 0 or p
            #x + rxt = 0, then t = -x/rx
            #x + rxt = p, then t = (p-x)/rx
            # y + ryt = 0, then t = -y/ry
            t = float('inf')
            for v in [F(-x,rx), F(-y,ry), F(p-x,rx), F(p-y,ry)]:
                if v > 0: t = min(t, v)

            x += rx * t
            y += ry * t

            #update rx, ry
            if x == p or x == 0: # bounced from east/west wall, so reflect on y axis
                rx *= -1
            if y == p or y == 0:
                ry *= -1

        return 1 if x==y==p else 0 if x==p else 2
        # return targets.index((x, y))
