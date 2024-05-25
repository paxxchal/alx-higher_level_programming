#!/usr/bin/node

const request = require('request');

// Get the URL from the first argument
const url = process.argv[2];

// Check if the URL argument is provided
if (!url) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

// Make a GET request to the URL
request(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Print the status code of the response
  console.log(`code: ${response.statusCode}`);
});
