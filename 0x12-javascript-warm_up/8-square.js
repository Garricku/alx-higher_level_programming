#!/usr/bin/node
/* Write a script that prints a square.
 * If the first argument can’t be converted to an integer, print “Missing size”
 * You must use the character X to print the square
 * You must use console.log(...) to print all output
 * You are not allowed to use var
 * You must use a loop (while, for, etc.)
 */
const size = parseInt(process.argv[2]);
const errMessage = 'Missing size';
let width = 1;
let height = 0;
let printX = 'X';

if (isNaN(size)) {
  console.log(errMessage);
} else {
  while (width < size) {
    printX += 'X';
    width++;
  }
  while (height < size) {
    console.log(printX);
    height++;
  }
}
