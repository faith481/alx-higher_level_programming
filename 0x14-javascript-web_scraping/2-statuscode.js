#!/usr/bin/node
// Script that displays the status code of a GET request
const httprequest = require('request');
if (process.argv.length > 2) {
  httprequest
    .get(process.argv[2])
    .on('response', serverResponse => {
      console.log(`code: ${serverResponse.statusCode}`);
    });
}
