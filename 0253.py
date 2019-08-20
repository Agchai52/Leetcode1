class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Method 1: Scan end
        #if not intervals: return 0
        #if len(intervals) == 1: return 1
        #start, end = [], []
        #for i in intervals:
        #    start.append(i[0])
        #    end.append(i[1])
        #start.sort()
        #end.sort()
        #e = 0
        #min_room = 0
        #'''
        #s, e = 0, 0
        #min_rooms, cnt_rooms = 0, 0
        #while s < len(starts):
        #    if starts[s] < ends[e]:
        #        cnt_rooms += 1  # Acquire a room.
        #        # Update the min number of rooms.
        #        min_rooms = max(min_rooms, cnt_rooms)
        #        s += 1
        #    else:
        #        cnt_rooms -= 1  # Release a room.
        #        e += 1
        #'''
        #for s in xrange(len(start)):
        #    if start[s] < end[e]:
        #        min_room += 1
        #    else:
        #        e += 1
        #return min_room
                
        # Method 2: Priority Queue
        import heapq
        if not intervals: return 0
        if len(intervals) == 1: return 1
        intervals.sort(key = lambda x: x[0])
        heap = []
        print(intervals)
        for interv in intervals:            
            if heap and interv[0] >= heap[0]:
                heapq.heapreplace(heap, interv[1])
            else:
                heapq.heappush(heap, interv[1])   
        return len(heap)
        
                
        
        
