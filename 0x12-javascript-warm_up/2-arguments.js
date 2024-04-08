#!/usr/bin/node
// print no arg, arg or args base on passed cli args
const process = require('node:process');

let message;

if (process.argv.length === 2) {
  message = 'No argument';
} else if (process.argv.length === 3) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}

console.log(message);
