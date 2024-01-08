#!/usr/bin/node
// Write a script that prints two arguments passed to it, in the following
// format: “argument1 is argument2”
const args = process.argv;
const argLink = ' is ';
console.log(args[2] + argLink + args[3]);
