class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals: return True
        if len(intervals) == 1: return True
        intervals.sort(key = lambda x: x[0])
        last = None
        for interv in intervals:
            if not last or interv[0] >= last:
                last = interv[1]
            elif last and interv[0] < last: 
                return False
        return True
                
            
