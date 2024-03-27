#!/usr/bin/node
// Script that computes the number of tasks completed by user id
const httpRequest = require('request');
if (process.argv.length > 2) {
  httpRequest(process.argv[2], (err, httpResponse, httpContent) => {
    const taskcount = {};
    if (err) {
      console.log(err);
    }
    JSON.parse(httpContent).forEach(task => {
      if (task.completed) {
        if (!taskcount[task.userId]) {
          taskcount[task.userId] = 0;
        }
        taskcount[task.userId]++;
      }
    });
    console.log(taskcount);
  });
}
