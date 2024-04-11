#!/usr/bin/node

const fs = require('fs');

function concatFiles (sourceFile1, sourceFile2, destinationFile) {
  try {
    const content1 = fs.readFileSync(sourceFile1, 'utf8');
    const content2 = fs.readFileSync(sourceFile2, 'utf8');
    const concatenatedContent = content1 + content2;
    fs.writeFileSync(destinationFile, concatenatedContent);
    console.log(`Files ${sourceFile1} and ${sourceFile2} successfully concatenated to ${destinationFile}.`);
  } catch (error) {
    console.error('Error concatenating files:', error.message);
  }
}

// Usage: node 102-concat.js fileA fileB fileC
const [sourceFile1, sourceFile2, destinationFile] = process.argv.slice(2);
concatFiles(sourceFile1, sourceFile2, destinationFile);
