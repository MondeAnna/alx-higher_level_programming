#!/usr/bin/node
// map object values to object keys
const dict = require('./101-data.js').dict;
const newDict = {};

for (const [key, value] of Object.entries(dict)) {
  if (!newDict[value]) {
    newDict[value] = [key];
  } else {
    newDict[value].push(key);
  }
}

console.log(newDict);
