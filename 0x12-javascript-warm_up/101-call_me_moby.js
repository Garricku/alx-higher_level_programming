#!/usr/bin/node
// Write a function that executes x times a function.

function callMeMoby (x, theFunction) {
  let count = 0;
  const intervalId = setInterval(() => {
    theFunction();
    count++;
    if (count === x) {
      clearInterval(intervalId);
    }
  }, 100);
}

module.exports = { callMeMoby };
