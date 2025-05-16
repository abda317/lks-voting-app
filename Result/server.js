const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const redis = require('redis');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);
const redisClient = redis.createClient({ host: 'redis' });

app.use(express.static('views'));

io.on('connection', (socket) => {
  console.log('Client connected');
});

redisClient.subscribe('votes');
redisClient.on('message', (channel, message) => {
  io.emit('vote', message);
});

server.listen(5001, () => {
  console.log('Result server running on port 5001');
});
