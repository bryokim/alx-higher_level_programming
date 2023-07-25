#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  if (body) {
    const results = JSON.parse(body).results;
    const num = results.filter(movie => movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')).length;
    console.log(num);
  }
});
