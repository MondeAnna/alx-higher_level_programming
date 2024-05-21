#!/usr/bin/node
// compute tyasks completed by user id

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }

  const resp = JSON.parse(body);
  const map = {};

  resp.forEach(entry => {
    const userId = entry.userId;
    if (entry.completed) {
      map[userId] = (map[userId] ?? 0) + 1;
    }
  });

  console.log(map);
});
