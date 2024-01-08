#!/usr/bin/node
// Write a script that computes and prints a factorial

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
      return 1;
  } else {
      return n * factorial(n - 1);
  }
}

const num = parseInt(process.argv[2]);
if (num > 100) {
  console.log('Infinity')
} else {
  console.log(factorial(num));
}
