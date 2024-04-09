#!/usr/bin/node
// concatenate two files
const process = require('node:process');
const fs = require('node:fs');

const pathToFileA = `./${process.argv[2]}`;
const pathToFileB = `./${process.argv[3]}`;
const pathToFileC = `./${process.argv[4]}`;

const fileA = fs.readFileSync(pathToFileA, 'utf-8');
const fileB = fs.readFileSync(pathToFileB, 'utf-8');

fs.writeFileSync(pathToFileC, fileA + fileB);
