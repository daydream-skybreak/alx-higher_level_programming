#!/usr/bin/node

const arg = process.argv[2];
if (arg === undefined || arg.isNaN === undefined) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(arg)}`);
}
