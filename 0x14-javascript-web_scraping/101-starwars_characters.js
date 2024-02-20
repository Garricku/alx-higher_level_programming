#!/usr/bin/node

const request = require('request');

function printCharactersForMovie (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request.get(apiUrl, { json: true }, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      body.characters.forEach((characterUrl) => {
        request.get(characterUrl, { json: true }, (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            console.log(charBody.name);
          }
        });
      });
    }
  });
}

// Usage: node printCharacters.js 3
const movieId = process.argv[2];
if (movieId) {
  printCharactersForMovie(movieId);
}
