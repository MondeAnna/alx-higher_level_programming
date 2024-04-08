#!/usr/bin/node
// convert cli digit to int
const process = require('node:process');

const integer = process.argv[2];

if (isNaN(integer)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + integer);
}
