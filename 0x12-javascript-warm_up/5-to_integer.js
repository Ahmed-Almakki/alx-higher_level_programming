#!/usr/bin/node

const text = Math.trunc(process.argv[2]);
if (isNaN(text)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${text}`);
}
