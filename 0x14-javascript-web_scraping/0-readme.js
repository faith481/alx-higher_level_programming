#!/usr/bin/node
// Script that reads and prints the content of a file
const fs = require('fs');
if (process.argv.length > 2) {
  fs.readFile(process.argv[2], (err, fctnt) => {
    if (err) {
      console.log(err);
    } else {
      console.log(fctnt.toString('utf-8'));
    }
  });
}
