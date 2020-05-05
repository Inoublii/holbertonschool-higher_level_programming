#!/usr/bin/node
export function callMeMoby (x, theFunction) {
  for (let count = 0; count < x; count++) {
    theFunction();
  }
}
