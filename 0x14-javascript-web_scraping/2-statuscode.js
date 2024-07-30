#!/usr/bin/node

const requests = require('request');

requests(process.argv[2], function (error, response) {
  if (error) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
