#!/usr/bin/node
function factorial (x) {
  if (x === 1 || isNaN(x)) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
const num = parseInt(process.argv[2]);
console.log(factorial(num));
