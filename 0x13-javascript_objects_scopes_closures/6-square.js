#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    if (c) {
      const side = `${c}`.repeat(this.width);
      for (let i = 0; i < this.height; i++) console.log(side);
    } else {
      this.print();
    }
  }
}

module.exports = Square;
