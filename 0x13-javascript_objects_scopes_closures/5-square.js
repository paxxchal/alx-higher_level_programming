#!/usr/bin/node

// Import the Rectangle class
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // Call the parent class (Rectangle) constructor with the same size for width and height
    super(size, size);
  }
}

module.exports = Square;
