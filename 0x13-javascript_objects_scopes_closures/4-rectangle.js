#!/usr/bin/node
// augment class properties
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
};
