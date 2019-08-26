class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # Method 1: Brute Force TLE Time = O(N^2) Space = O(N)
        #envs = envelopes
        #if len(envs) == 0: return 0
        #if len(envs) == 1: return 1
        #
        #res = [1] * len(envs)
        #envs.sort(key = lambda x:x[0])
        #
        #for i in xrange(len(envs)):
        #    for j in xrange(0, i):
        #        if envs[j][0] == envs[i][0]:
        #            continue
        #        if envs[j][1] < envs[i][1]:
        #            res[i] = max(res[i], res[j]+1)
        ##print(envs)
        ##print(res)
        #return max(res)
        
        # Method 2: DP + Binary Similar to #300 NlogN
        envs = envelopes
        if len(envs) == 0: return 0
        if len(envs) == 1: return 1
        
        envs.sort(lambda x,y: x[0] - y[0] if x[0]!=y[0] \
                  else y[1]-x[1] ) # same width, higher is first deal with repeated same width 
        
        ans = []
        for _, h in envs:
            l = 0
            r = len(ans)-1
            while l <= r:
                mid = (l + r) / 2
                if ans[mid] < h:
                    l = mid + 1
                else:
                    r = mid - 1
            if l >= len(ans):
                ans.append(h)
            else:
                ans[l] = h
        #print(ans)
        return len(ans)
            
#if __name__ == '__main__':
#    #envs = [[5,4],[6,4],[6,7],[2,3],[2,1]]
#    envs = [[2,3], [4,5], [4,4],[6,2],[7,4],[7,5]]
#    print(Solution().maxEnvelopes(envs))
