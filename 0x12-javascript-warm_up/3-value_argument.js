#!/usr/bin/node

const list = process.argv;
if (list[2] == null) {
  console.log('No argument');
} else {
  console.log(list[2]);
}
