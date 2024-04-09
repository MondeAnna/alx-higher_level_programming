#!/usr/bin/node
// convert from base 10
exports.converter = function (base) {
  return (n) => n.toString(base);
};
