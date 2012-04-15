#
# Twitter client for the led ticker deamon
# Author: 	Manuel Stofer
#

net    	= require 'net'
util    = require 'util'
twitter = require 'twitter'
fs		= require 'fs'
config 	= require 'yaml-config'

configFile = process.env.HOME + '/.ledticker/twitter.yaml'
try
	settings = config.readConfig configFile
catch err
	console.log 'could not load config file: ' + configFile
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
