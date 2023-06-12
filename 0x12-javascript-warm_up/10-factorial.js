#!/usr/bin/node

const { argv } = require('node:process');

function factorial (a) {
  if (a === 1) {
    return 1;
  }
  return factorial(a - 1) * a;
}

const num = parseInt(argv[2]);

if (Number.isNaN(num)) {
  console.log('1');
} else {
  console.log(factorial(num));
}
