#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  if (body) {
    const todos = JSON.parse(body);

    const done = {};
    for (const todo of todos) {
      if (todo.completed) {
        done[todo.userId] ? done[todo.userId]++ : (done[todo.userId] = 1);
      }
    }

    if (done) console.log(done);
  }
});
