#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the first argument
const movieId = process.argv[2];

// Check if the Movie ID argument is provided
if (!movieId) {
  console.error('Usage: ./100-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// URL for the Star Wars API
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Check if the request was successful
  if (response.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;

    // Function to fetch and print character names
    const fetchCharacterName = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (err, res, characterBody) => {
          if (err) {
            reject(err);
            return;
          }
          if (res.statusCode === 200) {
            const character = JSON.parse(characterBody);
            console.log(character.name);
            resolve();
          } else {
            reject(new Error(`Failed to fetch character. Status code: ${res.statusCode}`));
          }
        });
      });
    };

    // Fetch and print all character names sequentially
    characters.reduce((promise, characterUrl) => {
      return promise.then(() => fetchCharacterName(characterUrl));
    }, Promise.resolve());
  } else {
    console.log('Failed to retrieve the API. Status code:', response.statusCode);
  }
});
