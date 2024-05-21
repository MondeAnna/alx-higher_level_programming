#!/usr/bin/node
// prints all characters in a film

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId.toString();

request.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  console.log(JSON.parse(body).characters.forEach(character => {
    request.get(character, function (error, resp, obj) {
      if (error) {
        console.error(error);
      }

      console.log(JSON.parse(obj).name);
    });
  }));
});
