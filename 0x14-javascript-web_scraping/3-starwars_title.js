#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/:id'.replace(':id', process.argv[2]);

request(url, (err, res, body) => {
  if (err) console.log(err);
  if (body) console.log(JSON.parse(body).title);
});
