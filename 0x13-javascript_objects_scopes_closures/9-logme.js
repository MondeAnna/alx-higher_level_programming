#!/usr/bin/node
// show console log and log call count
let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
