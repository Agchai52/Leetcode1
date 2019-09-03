class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        '''
        1. only send message to age less than or equal to
        2. after sorted
        
        16, 16, 16, 16
        
        count = 4
        3
        2C4 = 4*3/2-n-1
        2C3 = 3*2/2-
        count - count-1
        '''
        # Method:LIS Brute Force TLE
        
        #if len(ages) <= 1: return 0
        #ages.sort()
        # 
        #N = len(ages)
        #res = 0
        #count = 1
        #
        #for i in range(1,N):
        #    if ages[i] < 14:
        #        continue
        #    if i > 0 and ages[i-1] == ages[i] and ages[i] > 14:
        #        count += 1 
        #    elif count > 1:
        #        res += count*(count-1)/2
        #        count = 1                
        #    for j in range(i):
        #        if ages[i] * 0.5 + 7 >= ages[j]:
        #            continue
        #        res += 1        
        #if count > 1 :
        #        res += count*(count-1)/2
        #        count = 0
        #return res
        
        # Method 2: hash table, since age<=120
        if len(ages)<= 1: return 0
        count = [0] * 121
        for age in ages:
            count[age] += 1
        res = 0
        for i, count_i in enumerate(count):
            for j, count_j in enumerate(count):
                if i * 0.5 + 7 >= j or i < j: continue
                res += count_i * count_j
                if i == j:
                    res -= count_i
        return res
