#!/usr/bin/node
// prints all characters in a film in presented order

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId.toString();

async function printCharacter (character) {
  await request.get(character, function (error, resp, obj) {
    if (error) {
      console.error(error);
    }

    console.log(JSON.parse(obj).name);
  });
}

request.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  JSON.parse(body).characters.forEach(character => printCharacter(character));
});
