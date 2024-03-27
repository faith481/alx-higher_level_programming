#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file
const fs = require('fs');
const httpRequest = require('request');
if (process.argv.length > 3) {
  httpRequest
    .get(`${process.argv[2]}`)
    .pipe(fs.createWriteStream(process.argv[3]));
}
