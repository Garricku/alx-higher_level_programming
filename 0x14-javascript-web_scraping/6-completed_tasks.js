#!/usr/bin/node
const request = require('request');

function countCompletedTasks (apiUrl) {
  request.get(apiUrl, { json: true }, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const completedTasks = body.filter(task => task.completed);
      const userTasks = {};

      completedTasks.forEach(task => {
        if (userTasks[task.userId]) {
          userTasks[task.userId]++;
        } else {
          userTasks[task.userId] = 1;
        }
      });
      for (const userId in userTasks) {
        console.log(`'${userId}': ${userTasks[userId]},`);
      }
    }
  });
}

// Usage: node countCompletedTasks.js https://jsonplaceholder.typicode.com/todos
const apiUrl = process.argv[2];
if (apiUrl) {
  countCompletedTasks(apiUrl);
}
