#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const completedTask = {};
    todos.forEach(function (todo) {
      if (todo.completed === true && completedTask[todo.userId] === undefined) {
        completedTask[todo.userId] = 1;
      } else if (todo.completed === true) {
        completedTask[todo.userId] += 1;
      }
    });
    console.log(completedTask);
  }
});
