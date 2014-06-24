# LED Ticker Daemon

- This was a student project i did some time ago.
- Its a network daemon for the AM03128-H11 led ticker. 
- Includes clients to receive tweets and sms's.
- Other led tickers might be compatible.

The project was about learning new languages, thats why the daemon is written
in Python, while the clients are coffee script.


## My Installation

I installed the LED-Ticker on a [Raspberry Pi](http://www.raspberrypi.org/ "Raspberry Pi")

This is how it looks like in action: [Video](http://www.youtube.com/watch?v=0U8NBKy94rw "LED-Ticker Raspberry Pi")





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
