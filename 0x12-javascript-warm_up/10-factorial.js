#!/usr/bin/node
function factorial (x) {
  if (isNaN(x)) {
    return 1;
  }
  if (x === 1) {
    return 1;
  }
  return x * factorial(x - 1);
}
const variable = Math.trunc(process.argv[2]);
const result = factorial(variable);
console.log(result);
