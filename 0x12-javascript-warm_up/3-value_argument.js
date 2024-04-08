#!/usr/bin/node
// print first argument passed
const process = require('node:process');

const message = process.argv[2] ? process.argv[2] : 'No argument';
console.log(message);
