#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const row = [];
    for (let i = 0; i <= this.width; i++) {
      row.push('');
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row.join('X'));
    }
  }
}
module.exports = Rectangle;
