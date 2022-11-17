#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url).on('response', () => {
    console.log(`code: ${response.statusCode}`);
});
