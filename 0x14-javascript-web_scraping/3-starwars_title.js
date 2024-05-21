#!/usr/bin/node
// startwars movie titles

const request = require('request');
const episodeNumber = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + episodeNumber;

request.get(url, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const title = JSON.parse(body).title;
  console.log(title);
});
