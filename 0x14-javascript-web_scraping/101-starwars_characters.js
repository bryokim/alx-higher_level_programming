#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function getCharacterName (character) {
  return new Promise((resolve) => {
    request(character, function (err, res, body) {
      if (err) console.log(err);
      if (body) resolve(JSON.parse(body).name);
    });
  });
}

request(url, async (err, res, body) => {
  if (err) console.log(err);
  if (body) {
    const characters = JSON.parse(body).characters;

    for (const character of characters) {
      const name = await getCharacterName(character);
      console.log(name);
    }
  }
});
