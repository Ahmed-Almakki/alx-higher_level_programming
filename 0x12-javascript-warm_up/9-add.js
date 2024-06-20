#!/usr/bin/node

function add (x, y) {
  return x + y;
}
const first = Math.trunc(process.argv[2]);
const second = Math.trunc(process.argv[3]);
const reult = add(first, second);
console.log(reult);
