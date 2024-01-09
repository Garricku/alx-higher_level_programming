#!/usr/bin/node
// Write a script that imports a dictionary of occurrences by user id
const dict = require('./101-data').dict;

const newDict = {};

for (const key in dict) {
  const value = dict[key];

  if (newDict[value] === undefined) {
    newDict[value] = [key];
  } else {
    newDict[value].push(key);
  }
}

console.log(newDict);
