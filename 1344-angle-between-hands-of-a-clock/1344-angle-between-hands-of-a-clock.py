class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Calculate the absolute position of both hands in degrees relative to 12:00
        # If hour is 12, reset it to 0 for base calculation
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        minute_angle = minutes * 6
        
        # Find the absolute difference between the two angles
        angle = abs(hour_angle - minute_angle)
        
        # Return the smaller of the two possible angles between the hands
        return min(angle, 360 - angle)
            