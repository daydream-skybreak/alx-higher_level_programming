#!/usr/bin/node
function second (x) {
  let length = x.length;
  if (x.length === 0 || x.length === 1) {
    return 0;
  } else {
    x.sort((a, b) => a - b);
    while (x[length - 1] === x[length - 2]) {
      length--;
    }
    return x[length - 2];
  }
}

const nums = process.argv.slice(2);
console.log(second(nums));
