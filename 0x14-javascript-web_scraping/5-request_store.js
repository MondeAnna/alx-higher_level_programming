#!/usr/bin/node
// store response content to file

const fs = require('fs');
const request = require('request');

const filename = process.argv[3];
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  fs.writeFile(filename, body, (error) => {
    if (error) {
      console.error(error);
    }
  });
});
