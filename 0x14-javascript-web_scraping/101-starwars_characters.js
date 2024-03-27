#!/usr/bin/node
// Script that prints all characters of a Star Wars movie
const httpRequest = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';
if (process.argv.length > 2) {
  httpRequest(`${API_URL}/films/${process.argv[2]}/`, (err, httpResponse, httpContent) => {
    if (err) {
      console.log(err);
    }
    const characterURLs = JSON.parse(httpContent).characters;
    const characterNames = characterURLs.map(
      url => new Promise((resolve, reject) => {
        httpRequest(url, (err, httpResponse, httpContent) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(httpContent).name);
        });
      }));
    Promise.all(characterNames)
      .then(names => console.log(names.join('\n')))
      .catch(err => console.log(err));
  });
}
