# LED Ticker Daemon

![Led Ticker](http://share.takimata.ch/ledticker.jpg "Led Ticker")

- This my student project. 
- Its a network daemon for AM03128-H11 led ticker. 
- Includes clients for twitter and SMS.
- Other led tickers might be compatible.

The project was about learning new languages, thats the reason
why i choose python for the daemon, while the clients are written in coffee script.


## Daemon

The daemon uses Twisted and pySerial.

### Installation
Make sure you have twisted installed.

run:
```
$ python daemon.py
```

## Clients

### Twitter client

#### Installation

- copy config/twitter.json to $HOME/.ledticker/twitter.json
- install dependencies with: ``` $ npm install ```
- create a twitter app and update the config file (https://dev.twitter.com/apps).

run:
```
$ coffee twitter.coffee
```

### SMS client

#### Installation

- copy config/sms.json to $HOME/.ledticker/sms.json
- install gammu.
- install the dependencies with: ``` $ npm install ```

run:
```
$ coffee sms.coffee
```


## License

  (The MIT License)

  Copyright (c) 2011 Manuel Stofer &lt;manuel@takimata.ch&gt;

  Permission is hereby granted, free of charge, to any person obtaining
  a copy of this software and associated documentation files (the
  'Software'), to deal in the Software without restriction, including
  without limitation the rights to use, copy, modify, merge, publish,
  distribute, sublicense, and/or sell copies of the Software, and to
  permit persons to whom the Software is furnished to do so, subject to
  the following conditions:

  The above copyright notice and this permission notice shall be
  included in all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.