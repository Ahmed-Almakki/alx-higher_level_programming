#!/usr/bin/node
function compare(a, b) {
  return a - b;
}

if (process.argv[2] == null) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  let list = [];
  let i;
  for (i = 2; i < process.argv.length; i++) {
    list[i - 2] = Math.trunc(process.argv[i]);
  }
  list = list.sort();
  list = list.sort(compare);
  const result = list.length - 2;
  console.log(list[result]);
}
