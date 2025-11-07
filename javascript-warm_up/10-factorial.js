#!/usr/bin/node
const { argv } = require('node:process');

function factorial (num) {
  num = parseInt(num);
  if (isNaN(num) || num === 0 || num < 0) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(argv[2]));
