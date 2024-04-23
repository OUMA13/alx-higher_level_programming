#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results || [];
    console.log(films.reduce(function (count, movie) {
      if (movie.characters.find(function (character) {
        return character.endsWith('/18/');
      })) {
        return count + 1;
      } else {
        return count;
      }
    }, 0));
  }
});
