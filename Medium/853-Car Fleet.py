# https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        postitionTarget = sorted(zip(position, speed), key=lambda x: x[0])
        maxHourSeen = (target-postitionTarget[-1][0])/postitionTarget[-1][1]
        count = 1
        for i in range(len(position)-1, -1, -1):
            hoursNeeded = (target-postitionTarget[i][0])/postitionTarget[i][1]
            if hoursNeeded > maxHourSeen:
                count += 1
                maxHourSeen = hoursNeeded

        return count
