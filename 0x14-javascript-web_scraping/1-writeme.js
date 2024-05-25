#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Check if both arguments are provided
if (!filePath || !stringToWrite) {
  console.error('Usage: ./1-writeme.js <file path> <string to write>');
  process.exit(1);
}

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
