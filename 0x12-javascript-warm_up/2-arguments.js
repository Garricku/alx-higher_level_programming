#!/usr/bin/node
/*
 * Task 2: Arguments
 * Write a script that prints a message depending of the number of arguments
 * passed.
 */
const { argv } = require('node:process');
const noArg = 'No argument';
const oneArg = 'Argument found';
const multipleArgs = 'Arguments found';

if (argv.length <= 2) {
  console.log(noArg);
} else if (argv.length === 3) {
  console.log(oneArg);
} else {
  console.log(multipleArgs);
}
