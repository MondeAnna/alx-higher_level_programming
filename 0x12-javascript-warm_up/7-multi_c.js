#!/usr/bin/node
// dynamic multi line print out
const process = require('node:process');
const integer = process.argv[2];

if (isNaN(integer)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < integer; i++) {
    console.log('C is fun');
  }
}
