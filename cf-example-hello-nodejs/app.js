var express = require("express");
var app = express();

var PORT = process.env.PORT || 3000;

app.get('/', function (req, res) {
  res.send(200, '<h2>This is Node.js running express</h2>');
});

app.listen(PORT, function () {
  console.log('Server running on http://localhost:' + PORT);
});
