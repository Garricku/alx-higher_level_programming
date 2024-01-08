#!/usr/bin/node
// Write a function that executes x times a function.

function callMeMoby (x, theFunction) {
  for (let count = 0; count < x; count++) {
    theFunction();
  }
}

module.exports = { callMeMoby };
