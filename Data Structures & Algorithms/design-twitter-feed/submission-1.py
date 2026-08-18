import heapq
class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) # {1: (2, 3), 2: (1, 3), 3: (1)}
        self.tweetMap = defaultdict(list) # {1: [(0, 10), (-1, 20)]}
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        tweetsHeap = []
        result = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                for post in self.tweetMap[followeeId]:
                    tweetsHeap.append(post)
        
        heapq.heapify(tweetsHeap)
        while tweetsHeap and len(result) < 10:
            count, tweetId = heapq.heappop(tweetsHeap)
            result.append(tweetId)

        return result

            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

         

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
