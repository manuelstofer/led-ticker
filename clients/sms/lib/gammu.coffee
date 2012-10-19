#
# Gammu wrapper to receive sms from modem
# Author: Manuel Stofer
#

_     = require 'underscore'
sys   = require 'util'
exec  = require('child_process').exec


gammu = {}

gammu._getallsms = (callback)->
  exec 'gammu getallsms', (error, stdout, stderr)->
    error = stderr if not error?
    callback error, stdout

gammu._parseSMSOutput = (error, output, callback)->
  blocks = output.split /\n\n/

  # the status is ignored
  blocks.pop()
  blocks.pop()

  messages = []
  while blocks.length
    messages.push {
      headers: blocks.shift()
      body:  blocks.shift()
    }

  callback(_.map messages, gammu._parseMessage)

gammu._parseMessage = (message)->
  headers = {}
  lines = message.headers.split /\n/
  lines = _.each lines, (line)->
    match = line.match /([^ ]*) *: "?([^"]*)"?$/
    headers[match[1]] = match[2] if match?
  {
    headers: headers
    body: message.body.trim()
  }

gammu.getMessages = (callback)-> gammu._getallsms (error, output)->
  gammu._parseSMSOutput error, output, callback

module.exports = gammu
