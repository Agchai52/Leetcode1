import heapq
import time

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.twits = collections.defaultdict(list)
        self.kFv = collections.defaultdict(list)
        self.pq = []
        

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.twits[userId].append((-time.time(), tweetId))
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        pq = []
        if userId in self.twits:
            for (timeStamp, post) in self.twits[userId]:
                pq.append((timeStamp, post))
            
        count = len(pq)
        for f in self.kFv[userId]:
            for (timeStamp, post) in self.twits[f]:
                pq.append((timeStamp, post))
                count += 1
        pq = list(set(pq))
        count = len(pq)
        if count > 10:
            count = 10
        heapq.heapify(pq)
        if pq:
            return [heapq.heappop(pq)[1] for _ in xrange(count)]
        else:
            return []
      
            

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId:
            self.kFv[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.kFv:
            if followeeId in self.kFv[followerId]:
                self.kFv[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
