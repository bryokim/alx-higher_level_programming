#!/usr/bin/node

const { argv } = require('node:process');

function secondLargest (arr) {
  let largest = arr[0];
  let second = 0;

  arr.forEach(item => {
    if (largest < item) {
      second = largest;
      largest = item;
    } else if (second < item && item !== largest) {
      second = item;
    }
  });
  return second;
}

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  console.log(secondLargest(argv.slice(2)));
}
