#!/usr/bin/node
// Write a script that concats 2 files
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const contentsA = fs.readFileSync(fileA, 'utf8');
const contentsB = fs.readFileSync(fileB, 'utf8');

const contentsC = contentsA + contentsB;

fs.writeFileSync(fileC, contentsC);
