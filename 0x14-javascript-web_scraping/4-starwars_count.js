#!/usr/bin/node
// Script that prints movies with "Wedge Antilles"
const httpRequest = require('request');
if (process.argv.length > 2) {
  httpRequest(`${process.argv[2]}`, (err, httpResponse, httpContent) => {
    if (err) {
      console.log(err);
    } else if (httpContent) {
      const movie = JSON.parse(httpContent).results.filter(
        x => x.characters.find(y => y.match(/\/people\/18\/?$/))
      );
      console.log(movie.length);
    }
  });
}
