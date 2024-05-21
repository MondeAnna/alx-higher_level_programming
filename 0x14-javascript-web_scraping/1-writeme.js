#!/usr/bin/node
// write text to file

const fs = require('fs');
const filename = process.argv[2];
const message = process.argv[3];

fs.writeFile(filename, message, (err) => {
  if (err) {
    console.error(err);
  }
});
