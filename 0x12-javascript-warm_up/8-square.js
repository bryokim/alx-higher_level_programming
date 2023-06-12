#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  let side = '';
  for (let i = 0; i < size; side += 'x', i++);
  for (let i = 0; i < size; i++) console.log(side);
}
