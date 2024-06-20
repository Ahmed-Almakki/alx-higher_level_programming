#!/usr/bin/node
const text = Math.trunc(process.argv[2]);
let count = 0;
if (isNaN(text)) {
  console.log('Missing number of occurrences');
} else {
  for (count; count < text; count++) {
    console.log('C is fun');
  }
}
