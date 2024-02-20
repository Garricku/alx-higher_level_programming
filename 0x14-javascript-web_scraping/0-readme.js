#!/usr/bin/node
const fs = require('fs');

function readAndPrintFileContent (filePath) {
  fs.readFile(filePath, 'utf8', (err, content) => {
    if (err) {
      console.error(err);
    } else {
      console.log(content);
    }
  });
}
const filePath = process.argv[2];
if (!filePath) {
  console.error('Please provide a valid file path as an argument.');
} else {
  readAndPrintFileContent(filePath);
}
