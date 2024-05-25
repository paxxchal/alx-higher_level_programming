#!/usr/bin/node

const request = require('request');

// Get the API URL from the first argument
const apiUrl = process.argv[2];

// Check if the API URL argument is provided
if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API URL>');
  process.exit(1);
}

// Character ID for Wedge Antilles
const wedgeAntillesId = 18;

// Make a request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Check if the request was successful
  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    // Iterate over the films to count appearances of Wedge Antilles
    films.forEach(film => {
      const characters = film.characters;
      if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
        count++;
      }
    });

    console.log(count);
  } else {
    console.log('Failed to retrieve the API. Status code:', response.statusCode);
  }
});
