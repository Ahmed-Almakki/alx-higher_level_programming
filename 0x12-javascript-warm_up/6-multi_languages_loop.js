#!/usr/bin/node
let i = 0;
const arry = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (i; i <= process.argv.length; i++) {
  console.log(arry[i]);
}
