#!/usr/bin/node

// Get the size of the square from the command line argument
const size = process.argv[2];

// Check if the argument is a valid positive integer
if (!size || isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  // Print the square using 'X' characters
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
