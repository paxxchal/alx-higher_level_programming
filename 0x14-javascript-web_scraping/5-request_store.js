#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get the URL and file path from the arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Check if both arguments are provided
if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file path>');
  process.exit(1);
}

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Write the response body to the file in utf-8 encoding
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
