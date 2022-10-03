#!/usr/bin/node
let len = 0;
while (process.argv[len] !== undefined) {
  len++;
}
if (len === 2) {
  console.log('No argument');
} else {
  for (let i = 2; i < len; i++) {
    console.log(process.argv[i]);
  }
}
