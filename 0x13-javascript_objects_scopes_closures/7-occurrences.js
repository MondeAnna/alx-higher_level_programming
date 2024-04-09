#!/usr/bin/node
// number of list occurances
exports.nbOccurences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
