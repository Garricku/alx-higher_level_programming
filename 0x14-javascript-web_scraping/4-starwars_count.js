#!/usr/bin/node
const request = require('request');

function getMovieCountForCharacter (characterId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}`;
  request.get(apiUrl, (error, response, body) => {
    if (error) {
      // do nothing;
    } else if (response.statusCode === 200) {
      const characterData = JSON.parse(body);
      const movieCount = characterData.films.length;
      console.log(movieCount);
    }
  });
}
const characterId = 18;
getMovieCountForCharacter(characterId);
