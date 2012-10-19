#
# sms client for the led-ticker daemon
# - receives sms using gammu
# Author: Manuel Stofer
#

gammu   = require './lib/gammu'
net    = require 'net'
_    = require 'underscore'
fs    = require 'fs'

#
# connect to led ticker daemon
connectToLedTicker = (callback)->
  client = net.connect settings.daemon.port, settings.daemon.host, (err)-> callback client, err


#
# sends a message to the led ticker daemon
sendMessage = (client, message)->
  if message?
    from = sanitizeNumber message.headers.number
    from = contacts[from] if contacts[from]
    client.write from + ': ' + message.body + '\r\n'

sendMessages = (client, messages)->
  messages = _.filter messages, (message)->
    message.headers['Status'] != 'Read'

  _.each messages, (message)->
    sendMessage client, message


#
# the country prefix is removed since not all numbers
# in addresses include the prefix
sanitizeNumber = (phone)->
  if phone?
    phone = phone.replace(/// ///g, '')
    phone = phone.replace(///^\+?\+41///, '0')
    phone = phone.replace(///^0041///, '0')
    phone = phone.replace(///:::.*///, '')
  phone


#
# load config file
configFile = process.env.HOME + '/.ledticker/sms.json'
try
  settings = JSON.parse fs.readFileSync(configFile)
catch err
  console.log 'could not load config file: ' + configFile
  console.log err
  process.exit()

contacts = settings.contacts


#
# connects to the led ticker daemon and reads
# incomming sms messages from gammu
connectToLedTicker (client, err)->
  hasRequest = false
  setInterval ()->
    if not hasRequest
      hasRequest = true
      gammu.getMessages (messages)->
        hasRequest = false
        sendMessages client, messages
  , 3000

