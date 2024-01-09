#!/usr/bin/node
// Write an empty class Rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      // Do nothing
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
