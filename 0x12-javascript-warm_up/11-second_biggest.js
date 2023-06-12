#!/usr/bin/node

function secondLargest (arr) {
  let largest = arr[0];
  let second = 0;

  arr.forEach((item) => {
    if (largest < item) {
      second = largest;
      largest = item;
    } else if (second < item && item !== largest) {
      second = item;
    }
  });
  return (arr.length === 2 && second === 0) ? arr[1] : second;
}

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  console.log(secondLargest(process.argv.slice(2).map(Number)));
}
