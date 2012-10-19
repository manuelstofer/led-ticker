#
# Twitter client for the led ticker deamon
# Author: 	Manuel Stofer
#

net    	= require 'net'
util    = require 'util'
twitter = require 'twitter'
fs		= require 'fs'

configFile = process.env.HOME + '/.ledticker/twitter.json'
try
	settings = JSON.parse fs.readFileSync(configFile)
catch err
	console.log 'could not load config file: ' + configFile
	console.log err
	process.exit()

#
# the screen_name and message are displayed
formatTweet = (tweet)-> '@' + tweet.user.screen_name + ': ' + tweet.text + '\r\n'

#
# checks if a tweet is valid
isValidTweet = (tweet)-> tweet? and tweet.text? and tweet.user? and tweet.user.screen_name?

#
# connect to twitter stream
connectToTwitterStream = (callback)->
	twit = new twitter(settings.api)
	console.log 'tracking: ' + settings.track
	twit.stream 'user', {track: settings.track}, (stream)-> callback stream

#
# connect to led ticker daemon
connectToLedTicker = (callback)->
	client = net.connect settings.daemon.port, settings.daemon.host, (err)-> callback client, err

#
# connects to the led ticker deamon and to the twitter stream
connectToLedTicker (ticker)-> connectToTwitterStream (stream)->
	# add an event listener for new tweets
	stream.on 'data', (tweet) -> ticker.write formatTweet(tweet) if isValidTweet tweet
