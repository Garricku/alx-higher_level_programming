#!/usr/bin/node
const request = require('request');

function getStatus (url) {
  request.get(url, (error, response) => {
    if (error) {
      console.error('code:', error.statusCode);
    } else {
      console.log('code:', response.statusCode);
    }
  });
}

// Usage: node getStatus.js <URL>
const url = process.argv[2];
if (!url) {
  // do nothing
} else {
  getStatus(url);
}
