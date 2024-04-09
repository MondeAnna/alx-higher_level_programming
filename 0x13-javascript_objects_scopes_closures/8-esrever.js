#!/usr/bin/node
// reverse list elements
exports.esrever = function (list) {
  const reversed = [];
  for (let iter = list.length - 1; iter >= 0; iter--) {
    reversed.push(list[iter]);
  }
  return reversed;
};
