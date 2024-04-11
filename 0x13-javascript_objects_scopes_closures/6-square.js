#!/usr/bin/node

// Import the Rectangle class
const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    // Call the parent class (Rectangle) constructor with the same size for width and height
    super(size, size);
  }

  charPrint (c) {
    // If c is undefined, use 'X'; otherwise, print the rectangle using the specified character
    const charToPrint = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(charToPrint.repeat(this.width));
    }
  }
}

module.exports = Square;
