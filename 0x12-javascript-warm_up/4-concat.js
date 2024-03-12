#!/usr/bin/node

const { argv } = process;

if (argv[2]) {
  console.log(argv[2] + ' is ' + argv[3]);
} else {
  console.log('undefined is undefined');
}
