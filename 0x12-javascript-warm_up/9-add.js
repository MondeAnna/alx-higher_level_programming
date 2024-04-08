#!/usr/bin/node
// add two operands
const process = require('node:process');

const leftOperand = parseInt(process.argv[2]);
const rightOperand = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(leftOperand, rightOperand));
