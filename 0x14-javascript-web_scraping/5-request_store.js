#!/usr/bin/node

const request = require('request');
const fs = require('node:fs');

request(process.argv[2], function (error, reponse, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
