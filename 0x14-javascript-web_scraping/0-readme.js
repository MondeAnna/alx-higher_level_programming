#!/usr/bin/node
// read in ande print file contents

const fs = require('fs');
const filename = process.argv[2];

fs.readFile(filename, (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data.toString());
});
