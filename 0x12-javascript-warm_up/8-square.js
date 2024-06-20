#!/usr/bin/node

const text = Math.trunc(process.argv[2]);
let row;
let column;
if (isNaN(text)) {
  console.log('Missing size');
} else {
  for (row = 0; row < text; row++) {
    let line = '';
    for (column = 0; column < text; column++) {
      line += 'X';
    }
    console.log(line);
  }
}
