#!/usr/bin/node
/* Write a class Square that defines a square and inherits from Rectangle
 * of 5-square.js
 */
const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    let chara = 'C';
    let shape = '';
    let size = 0;
    if (!c) {
      chara = 'X';
    }
    while (size < this.width) {
      shape += chara;
      size++;
    }
    size = 0;
    while (size < this.height) {
      console.log(shape);
      size++;
    }
  }
}

module.exports = Square;
