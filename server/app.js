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
let clientTokens = {};
let sockets = [];

io.on("connection", (socket) => {
  console.log("New client connected");
  sockets.push(socket);

  if (interval) {
    clearInterval(interval);
  }

  // Update users every 1 second
  interval = setInterval(() => updateUsers(socket), 1000);

  // Add to clientTokens when user updated
  socket.on("new user", function(data) {
    if(!clientTokens.hasOwnProperty(data)) {
      clientTokens[socket.id] = data;
    }
  });

  // cleanup
  socket.on("disconnect", () => {
    clientTokens[socket.id] = undefined;
    console.log("Client disconnected");
  });
});

// Send users data
const updateUsers = socket => {
  io.sockets.emit("update", clientTokens);
}

server.listen(port, () => console.log(`Listening on port ${port}`));



