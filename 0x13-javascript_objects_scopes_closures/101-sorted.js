#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const i in dict) {
  if (dict[i].toString() in newDict) {
    newDict[dict[i]].push(i);
  } else {
    newDict[dict[i]] = [i];
  }
}

for (const j in newDict) {
  newDict[j].sort();
}
console.log(newDict);
