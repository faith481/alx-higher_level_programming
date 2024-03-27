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
    characterURLs.forEach(task => {
      httpRequest(task, (err, httpResponse, httpContent) => {
        if (err) {
          console.log(err);
        }
        console.log(JSON.parse(httpContent).name);
      });
    });
  });
}
