#!/usr/bin/node
const fs = require('fs');
const request = require('request');

function saveWebpageToFile (url, filePath) {
  request.get(url, { encoding: 'utf-8' }, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
        if (!err) {
          // do nothing
        }
      });
    }
  });
}

// Usage: node saveWebpage.js <URL> <file-path>
const url = process.argv[2];
const filePath = process.argv[3];

if (url && filePath) {
  saveWebpageToFile(url, filePath);
}
