#!/usr/bin/node
let x = 0;
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
}
while (x < arg) {
  console.log('C is fun');
  x++;
}
