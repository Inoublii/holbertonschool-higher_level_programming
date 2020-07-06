#!/usr/bin/node
const arg = process.argv[2];
const f = require('fs');

f.readFile(arg, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
