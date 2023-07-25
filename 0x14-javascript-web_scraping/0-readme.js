#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];

try {
  fs.readFile(filename, 'utf-8', (err, data) => {
    if (err) console.log(err);
    if (data) console.log(data);
  });
} catch (e) {
  console.log(e.toString());
}
