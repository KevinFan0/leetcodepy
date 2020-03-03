# 355 设计twitter
"""
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户
示例:

Twitter twitter = new Twitter();

// 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
twitter.postTweet(1, 5);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
twitter.getNewsFeed(1);

// 用户1关注了用户2.
twitter.follow(1, 2);

// 用户2发送了一个新推文 (推文id = 6).
twitter.postTweet(2, 6);

// 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
// 推文id6应当在推文id5之前，因为它是在5之后发送的.
twitter.getNewsFeed(1);

// 用户1取消关注了用户2.
twitter.unfollow(1, 2);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
// 因为用户1已经不再关注用户2.
twitter.getNewsFeed(1);
"""
import time
from queue import PriorityQueue

class Tweet:
    def __init__(self, id, time):
        self.id = id
        self.time = time
        self.next = None

class User:
    def __init__(self, id):
        self.id = id
        self.head = None
        self.followed = set()
        self.follow(id)

    def follow(self, userid):
       self.followed.add(userid)

    def unfollow(self, userid):
        if userid != self.id:
            self.followed.remove(userid)

    def post(self, tweetid):
        twt = Tweet(tweetid, time.time())
        twt.next = self.head
        self.head = twt

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp = 0
        self.usermap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.usermap.keys():
            self.usermap[userId] = User(userId)
        u = self.usermap.get(userId)
        u.post(tweetId)

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        res = []
        if userId not in self.usermap.keys():
            return res
        users = self.usermap.get(userId).followed
        # 自动通过time属性从大到小排序，容量为users的大小
        pq = PriorityQueue()
        for id in users:
            twt = self.usermap.get(id).head
            if not twt:
                continue
            pq.put(twt)
        while not pq:
            if len(res) == 10:
                break
            twt = pq.get()
            res.append(twt.id)
            if twt.next:
                pq.put(twt.next)
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.usermap.keys():
            self.usermap[followerId] = User(followerId)
        if followeeId not in self.usermap.keys():
            self.usermap[followeeId] = User(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.usermap.keys():
            flwer = self.usermap.get(followerId)
            flwer.unfollow(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)