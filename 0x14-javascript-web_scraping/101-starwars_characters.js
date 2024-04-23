#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error) {
    const result = JSON.parse(body).characters;
    printActors(result, 0);
  }
});

function printActors (actors, index) {
  request(actors[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < actors.length) {
        printActors(actors, index + 1);
      }
    }
  });
}
