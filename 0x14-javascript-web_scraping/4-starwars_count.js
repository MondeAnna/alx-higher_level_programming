#!/usr/bin/node
// number of films with the character id 18

const request = require('request');
const url = process.argv[2];
const id = '18';

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }

  const results = JSON.parse(body).results;
  let count = 0;

  for (let outer = 0; outer < results.length; outer++) {
    const characters = results[outer].characters;

    for (let inner = 0; inner < characters.length; inner++) {
      if (characters[inner].includes(id)) {
        count += 1;
      }
    }
  }

  console.log(count);
});
