#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w && w > 0) && (h && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const side = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) console.log(side);
  }
}

module.exports = Rectangle;
