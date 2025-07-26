import heapq
from typing import List


class Twitter:

    tweet_count = 0

    def __init__(self):
        self.tweets = {}
        self.followers = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        user_tweets = self.tweets.get(userId, [])

        Twitter.tweet_count += 1
        user_tweets.append((Twitter.tweet_count, tweetId))

        self.tweets[userId] = user_tweets

    def getNewsFeed(self, userId: int) -> List[int]:
        h, news_feed = [], []

        users = self.followers.get(userId, []).copy()
        users.append(userId)

        for user in users:
            tweets = self.tweets.get(user, [])

            if len(tweets) >= 1:
                idx = len(tweets) - 1
                id, tweet = tweets[idx]
                heapq.heappush(h, (-id, tweet, idx, user))

        while h and len(news_feed) < 10:
            _, tweet, idx, user = heapq.heappop(h)

            news_feed.append(tweet)
            idx -= 1

            if idx >= 0:
                id, tweet = self.tweets[user][idx]
                heapq.heappush(h, (-id, tweet, idx, user))

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        followers = self.followers.get(followerId, [])

        if followeeId not in followers:
            followers.append(followeeId)

        self.followers[followerId] = followers

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followers = self.followers.get(followerId, [])

        if followeeId in followers:
            followers.remove(followeeId)

        self.followers[followerId] = followers


twitter = Twitter()
twitter.postTweet(1, 5)

feed = twitter.getNewsFeed(1)
print(feed)

twitter.follow(1, 2)
twitter.postTweet(2, 6)

feed = twitter.getNewsFeed(1)
print(feed)

twitter.unfollow(1, 2)

feed = twitter.getNewsFeed(1)
print(feed)
