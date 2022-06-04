"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

The tricky part is determining how the minute hand affects the position of the hour hand.
Calculate the angles separately then find the difference.

"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        one_min_angle = 6
        one_hour_angle = 30
        
        minute_angle = one_min_angle * minutes
        hour_angle = one_hour_angle * (hour%12 + minutes/60)
        
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360-diff)
