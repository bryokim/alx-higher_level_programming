#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  return (a + b);
}

const first = parseInt(argv[2]);
const second = parseInt(argv[3]);

console.log(add(first, second));
