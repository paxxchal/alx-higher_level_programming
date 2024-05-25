#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2] || 'https://swapi-api.alx-tools.com/api/films/';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const wedgeMovies = data.results.filter((film) => {
      return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/18/`);
    });
    console.log(wedgeMovies.length);
  }
});
