# https://leetcode.com/problems/minimum-time-difference/

# CodeHelp
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # step1: convert time string into minutes integer value
        minutes = []

        for i in range(len(timePoints)):
            curr = timePoints[i]
            print(curr[0:2])

            hours = int(curr[:2])
            mins = int(curr[3:]) 
            totalMinutes = hours*60 + mins
            minutes.append(totalMinutes)
        

        # Step2: sort
        minutes.sort()

        # Step3: difference and calculate min diff
        mini = 2147483647
        n = len(minutes)

        for i in range(n-1):
            diff = minutes[i+1] - minutes[i]
            mini = min(mini, diff)

        # something missing - THIS IS THE GAME
        lastDiff1 = (minutes[0] + 1440) - minutes[n-1]
        lastDiff2 = minutes[n-1] - minutes[0]
        lastDiff = min(lastDiff1, lastDiff2)
        mini = min(mini, lastDiff)

        return mini
















