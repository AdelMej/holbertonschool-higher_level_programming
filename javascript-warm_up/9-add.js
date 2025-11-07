#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return Number(a) + Number(b);
}
const { argv } = require('node:process');
console.log(add(argv[2], argv[3]));
