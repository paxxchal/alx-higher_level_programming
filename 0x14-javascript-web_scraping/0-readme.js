#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

// Check if the file path argument is provided
if (!filePath) {
  console.error('Usage: ./0-readme.js <file path>');
  process.exit(1);
}

// Read the file content in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
