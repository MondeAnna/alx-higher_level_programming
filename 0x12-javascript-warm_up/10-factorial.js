#!/usr/bin/node
// factorial
const process = require('node:process');
const integer = process.argv[2] ? process.argv[2] : 0;

function factorial (n) {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(integer));
