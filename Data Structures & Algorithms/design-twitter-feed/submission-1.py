class DLL:
    def __init__(self,tweetId, userId):
        self.tweetId = tweetId
        self.sender = userId
        self.prev = None
        self.next = None


class Twitter:

    def __init__(self):
        self.friends = defaultdict(set)
        self.lastTweet = DLL(-1, 0)

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = DLL(tweetId, userId)
        tweet.prev, self.lastTweet.next = self.lastTweet, tweet
        self.lastTweet = tweet      
        return  

    def getNewsFeed(self, userId: int) -> List[int]:
        tweet = self.lastTweet
        tweets = []
        while tweet.tweetId != -1 and len(tweets) < 10:
            if tweet.sender == userId or tweet.sender in self.friends[userId]:
                tweets.append(tweet.tweetId)
            tweet = tweet.prev
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.friends[followerId].add(followeeId)
        return
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.friends[followerId].remove(followeeId)
        except:
            return
        return
        