#!/usr/bin/node
/*
 * Task 2: Arguments
 * Write a script that prints a message depending of the number of arguments
 * passed.
 */
const numArgs = process.argv.length - 2;
const noArg = 'No argument';
const oneArg = 'Argument found';
const multipleArgs = 'Arguments found';

if (numArgs <= 0) {
  console.log(noArg);
} else if (numArgs === 1) {
  console.log(oneArg);
} else {
  console.log(multipleArgs);
}
