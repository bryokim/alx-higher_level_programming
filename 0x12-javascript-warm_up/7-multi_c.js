#!/usr/bin/node

const { argv } = require('node:process');

const num = parseInt(argv[2]);

if (Number.isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < num; i++) console.log('C is fun');
}
