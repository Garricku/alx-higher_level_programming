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

  print () {
    let shape = 'X';
    let size = 1;
    while (size < this.width) {
      shape += 'X';
      size++;
    }
    size = 0;
    while (size < this.height) {
      console.log(shape);
      size++;
    }
  }
}

module.exports = Rectangle;
