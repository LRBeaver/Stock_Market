class Twitt:
    def __init__(self):
        self.usernames = []
        self.names = []
        self.tweet = []
        self.imageurl = []

    def twitter_lookup(self, coordinents, radius):
        cheese = []
        twitter = Twitter(auth=auth)
        coordinents = coordinents + "," + radius
        print(coordinents)
        query = twitter.search.tweets(q="", geocode=coordinents, rpp=10)
        for result in query["statuses"]:
            self.usernames.append(result["user"]["screen_name"])
            self.names.append(result['user']["name"])
            self.tweet.append(h.unescape(result["text"]))
            self.imageurl.append(result['user']["profile_image_url_https"])

k = Twitt()
# k.twitter_lookup("51.5033630,-0.1276250", "1mi")
# print(k.names)

for attr, value in k.__dict__.iteritems():
    print(attr, value)