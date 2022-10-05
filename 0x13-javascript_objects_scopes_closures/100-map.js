#!/usr/bin/node
const list = require('./100-data').list;
const list1 = list.map((item, i) => item * i);
console.log(list);
console.log(list1);
