#!/usr/bin/node
let x = 0;
const arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing size');
}
while (x < arg) {
  console.log('X'.repeat(arg));
  x++;
}
