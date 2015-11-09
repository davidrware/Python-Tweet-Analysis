from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "208782686-oTRGHg3oqMYpQhIzmewgysQgqDXp59oq9yzK4PuB"
access_token_secret = "SJ3WDAzpZFnlLrgQDTt7oQwBGpYomCn1Zsg5kVIPfTmUo"
consumer_key = "WiAbqByhUseWq51ljihGRIgGZ"
consumer_secret = "fjhSlxsVdd5yBvpxlAniAYBQOv6AukHMirKUZ2OwTRkrG7NmhD"

class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self,status):
        print status

if __name__ == "__main__":
    l = StdOutListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream = Stream(auth,l)

    stream.filter(track=['bernie','sanders','clinton','trump','obama'])
