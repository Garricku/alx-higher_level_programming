#!/usr/bin/node
// Write a script that searches the second biggest integer in the list of args
function secondBiggest () {
  const args = process.argv.slice(2).map(Number);
  if (args.length === 0) {
    console.log(0);
  } else if (args.length === 1) {
    console.log(0);
  } else {
    const max = Math.max(...args);
    let secondMax = -Infinity;
    for (let i = 0; i < args.length; i++) {
      if (args[i] > secondMax && args[i] < max) {
        secondMax = args[i];
      }
    }
    console.log(secondMax);
  }
}

secondBiggest();
