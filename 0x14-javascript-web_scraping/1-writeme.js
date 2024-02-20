#!/usr/bin/node
const fs = require('fs');

function writeToFile (filePath, content) {
  fs.writeFile(filePath, content, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error(err);
    }
  });
}

const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  // do nothing
} else {
  writeToFile(filePath, content);
}
