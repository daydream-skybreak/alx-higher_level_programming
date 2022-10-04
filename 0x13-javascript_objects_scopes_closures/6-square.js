#!/usr/bin/node
const s = require('./5-square');
class Square extends s {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let s = '';
      for (let i = 0; i < this.height; i++) {
        s += c;
      }
      console.log(s);
    }
  }
}
module.exports = Square;
