#!/usr/bin/node
/* 
 * Write a script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer.
 * If the argument can’t be converted to an integer, print “Not a number”
 */
const firstArg = parseInt(process.argv[2]);
const numErr = 'Not a number';
const message = 'My number: '

if (isNaN(firstArg)) {
  console.log(numErr);
} else {
  console.log(message + firstArg);
}
