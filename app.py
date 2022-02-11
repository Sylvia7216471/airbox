

var mqtt    = require('80');
var client  = mqtt.connect('ws://120.119.157.238');

client.on('connect', function () {
  client.subscribe('liru');
  client.publish('presence', 'Hello mqtt');
});

client.on('message', function (topic, message) {
  // message is Buffer
  console.log(message.toString());
  client.end();
});
