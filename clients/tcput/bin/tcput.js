#!/usr/local/bin/node

var net = require('net');
var stdin = process.openStdin();

var connected = false,
  finished = false,
  buffer = '',
  host = process.argv[2] || 'localhost',
  port = process.argv[3] || 3000;

var client = net.connect(port, host, function (err){
  console.log('connected to: ' + host + ' ' + port);
  connected = true;
  send(buffer);
});

var send = function (data) {
  if (!data.length){
    return;
  }
  console.log('send: "' + data +'"');

  client.write(data, function () {
    if (finished) {
      process.exit();
    }
  });
};

stdin.on('data', function (data) {
  data = data.toString().replace(/(\n\r?)+/g, '\r\n');
  if (connected) {
    send(buffer);
  } else {
    buffer += data;
  }
});

stdin.on('end', function () {
  finished = true;
});
