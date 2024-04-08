#!/usr/bin/node
// print first and second cli arg positions
const process = require('node:process');
console.log(process.argv[2] + ' is ' + process.argv[3]);
