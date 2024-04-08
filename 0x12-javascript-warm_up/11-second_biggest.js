#!/usr/bin/node
// second biggest value
const process = require('node:process');
const args = process.argv.splice(2, process.argv.length);

if (args.length <= 1) {
  console.log(0);
} else {
  const sorted = args.map(Number).sort((a, b) => a - b);
  console.log(sorted.reverse()[1]);
}
