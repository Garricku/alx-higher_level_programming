#!/usr/bin/node
const request = require('request');

function getMovieTitle (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request.get(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    }
  });
}

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a valid movie ID as an argument.');
} else {
  getMovieTitle(movieId);
}
