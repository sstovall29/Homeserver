
if (typeof io !== "undefined") {
  const socket = io();
  socket.on("connect", () => {
    console.log("Connected via Socket.IO");
  });

  socket.on("Hello Client", (data) => {
  console.log("Server said Hi");
  console.log(data);
});
}
