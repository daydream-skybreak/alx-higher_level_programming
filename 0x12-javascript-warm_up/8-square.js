#!/usr/bin/node
const side = process.argv[2];
const row = [];
if (isNaN(side)) {
  console.log('Missing side');
} else {
  for (let i = 0; i <= side; i++) {
    row.push('');
  }
  for (let i = 0; i < side; i++) {
    console.log(row.join('X'));
  }
}
