#!/usr/bin/node

const { argv } = require('node:process');

const size = parseInt(argv[2]);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  let side = '';
  for (let i = 0; i < size; side += 'x', i++);
  for (let i = 0; i < size; i++) console.log(side);
}
