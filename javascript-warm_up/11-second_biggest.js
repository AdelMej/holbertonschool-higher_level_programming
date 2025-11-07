#!/usr/bin/node
const { argv } = require('node:process');
let sec = -Infinity;
let max = -Infinity;

if (argv.length <= 3) {
  console.log(0);
} else {
  max = Number(argv[2]);
  for (let i = 3; i < argv.length; i++) {
    const n = argv[i];
    if (n > max) {
      sec = max;
      max = n;
    } else if (n < max && n > sec) {
      sec = n;
    }
  }
  if (isNaN(sec)) sec = 0;
  console.log(sec === -Infinity ? 0 : sec);
}
