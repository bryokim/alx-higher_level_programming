#!/usr/bin/node

const fs = require('fs');
const request = require('request');

if (process.argv.length < 4) {
  console.log('USAGE: ./5-request_store.js [URL] [FILE_PATH]');
  process.exit();
}

request(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  if (body) {
    const options = {
      encoding: 'utf-8'
    };
    fs.writeFile(process.argv[3], body, options, (err) => {
      if (err) console.log(err);
    });
  }
});
