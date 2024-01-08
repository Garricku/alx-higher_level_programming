#!/usr/bin/node
// Write a function that increments and calls a function.
function addMeMaybe (number, theFunction) {
  for (let count = 0; count < number; count++) {
    theFunction();
  }
}

module.exports = { addMeMaybe };
