#!/usr/bin/node
// increment parametric int
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
