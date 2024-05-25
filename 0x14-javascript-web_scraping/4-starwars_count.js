#!/usr/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.log('Usage: ./4-starwars_count.js API_URL');
  process.exit(1);
}

const apiUrl = process.argv[2];
const charId = 18; // Wedge Antilles character ID

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  const films = JSON.parse(body).results;
  const filmCount = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`)).length;

  console.log(filmCount);
});
