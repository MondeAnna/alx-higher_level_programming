#!/usr/bin/node
// map a new list
const list = require('./100-data.js').list;

console.log(list);
console.log(list.map((x, index) => x * index));
