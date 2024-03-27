#!/usr/bin/node
// Script that prints the title of a Star Wars movie for a given episode
const httpRequest = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';
if (process.argv.length > 2) {
  httpRequest(`${API_URL}/films/${process.argv[2]}/`, (err, httpResponse, httpContent) => {
    if (err) {
      console.log(err);
    }
    console.log(JSON.parse(httpContent).title);
  });
}
