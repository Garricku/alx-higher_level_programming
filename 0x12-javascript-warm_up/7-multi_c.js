#!/usr/bin/node
// Write a script that prints x times “C is fun”
const printThis = 'C is fun';
const repeat = process.argv[2];
let i = 0;

if (!repeat) {
  console.log('Missing number of occurrences');
} else {
  while (i < repeat) {
    console.log(printThis);
    i++;
  }
}
