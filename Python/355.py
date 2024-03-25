class Twitter:

    def __init__(self):
        self.usermap = {}
        self.ctr = 0

    def update_counter(self):
        self.ctr += 1

    def get_tweets_for_user(self, userId):
        return self.usermap[userId]['tweets']

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.usermap:
            self.usermap[userId] = {
                'tweets':[(self.ctr, tweetId)],
                'follows':[]
            }
        else:
            self.usermap[userId]['tweets'].append((self.ctr, tweetId))
        self.update_counter()

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.usermap:
            return []
        feed = self.usermap[userId]['tweets'].copy()
        for friend in self.usermap[userId]['follows']:
            if friend in self.usermap:
                feed += self.get_tweets_for_user(friend)
        heapq.heapify(feed)
        news_feed = heapq.nlargest(10, feed)
        sol = []
        for nf in news_feed:
            sol.append(nf[1])
        return sol
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.usermap:
            self.usermap[followerId] = {
                'tweets':[],
                'follows':[followeeId]
            }
        else:
            if followeeId not in self.usermap[followerId]['follows']:
                self.usermap[followerId]['follows'].append(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.usermap[followerId]['follows']:
            self.usermap[followerId]['follows'].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
