#!/usr/bin/node
const a = Number(process.argv[2]);
function factorialize (a) {
  if (isNaN(a) || a === 1) {
    return (1);
  } else {
    return (a * factorialize(a - 1));
  }
}
console.log(factorialize(a));
