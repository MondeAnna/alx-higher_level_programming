#!/usr/bin/node
// inheritance ii
const OriginalSquare = require('./5-square.js');

module.exports = class Square extends OriginalSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let row = 0; row < this.height; row++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
