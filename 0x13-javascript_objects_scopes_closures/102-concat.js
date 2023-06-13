#!/usr/bin/node

const { readFile, appendFile } = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (fileA && fileB && fileC) {
  [fileA, fileB].forEach(file => {
    readFile(file, 'utf8', (error, data) => {
      if (error) throw error;
      appendFile(fileC, data, (err) => {
        if (err) throw err;
      });
    });
  });
}
