#!/usr/bin/node
const { argv } = require('node:process');
if (!argv[2]) console.log('No argument');
else argv.slice(2).forEach(x => console.log(x));
