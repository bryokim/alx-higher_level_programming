#!/usr/bin/node

const fs = require('fs');

const args = process.argv;

if (args.length < 4) {
  console.error('Few arguments');
  process.exit();
}

fs.writeFile(args[2], args[3], (err) => {
  if (err) console.log(err);
});
