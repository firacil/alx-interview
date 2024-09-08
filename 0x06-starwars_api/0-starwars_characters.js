#!/usr/bin/node

const request = require('request');

const mvId = process.argv[2];
const mvend = 'https://swapi-api.alx-tools.com/api/films/' + mvId;

function letRequest (charList, index) {
  if (charList.length === index) {
    return;
  }

  request(charList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      letRequest(charList, index + 1);
    }
  });
}

request(mvend, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const charList = JSON.parse(body).characters;

    letRequest(charList, 0);
  }
});
