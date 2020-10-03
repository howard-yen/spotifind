const express = require("express");
const http = require("http");
const socketIo = require("socket.io");

const port = process.env.PORT || 4001;
const index = require("./routes/index");

const app = express();
app.use(index);

const server = http.createServer(app);

const io = socketIo(server);

let interval;
let users = [];

io.on("connection", (socket) => {
  console.log("New client connected");
  if (interval) {
    clearInterval(interval);
  }
  interval = setInterval(() => updateUsers(socket), 1000);
  socket.on("update user", function(data) {
    if(!users.includes(data)) {
      console.log("pushed");
      users.push(data);
    }
  });
  socket.on("disconnect user", function(data) {
    console.log("called");
    if(users.includes(data)) {
      const index = users.indexOf(data);
      users.splice(index, 1);
    }
  });
  socket.on("disconnect", () => {
    console.log("Client disconnected");
    clearInterval(interval);
  });
});

const getApiAndEmit = socket => {
  const response = new Date();
  // Emitting a new message. Will be consumed by the client
  socket.emit("FromAPI", response);
};

const updateUsers = socket => {
  io.sockets.emit("updateUsers", users);
}

server.listen(port, () => console.log(`Listening on port ${port}`));



