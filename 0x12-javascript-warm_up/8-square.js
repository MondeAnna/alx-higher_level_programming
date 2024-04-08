#!/usr/bin/node
// print a square
const process = require('node:process');
const size = process.argv[2];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
