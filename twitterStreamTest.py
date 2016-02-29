from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'FcnZE74GE730kbBqT6L2Jg'
csecret = 'vxTueRQhRSRWD3IfJ3jV2oGjO2YmgoDdDeHZJnCYg'
atoken = '2292908942-obzBWF2471BbjklBfje6wdLlbO9ta15D0MUdCcC'
asecret = 'P0PALSyhsKZEHTxJxkEx4sxzrLFqKhsx8BXb4J6ZSmKrS'

class listener(StreamListener):
	
	def on_data(self,data):
		hashtag = "#"
		if hashtag in data:
			try:
				print data
				saveFile = open('twitDB.csv','a')
				saveFile.write(data)
				saveFile.write('/n')
				saveFile.close()
				return True
			except BaseException, e:
				print 'failedondata,',str(e)
				time.sleep(5)

	def on_error(self,status):
		print status

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track =["car"])

