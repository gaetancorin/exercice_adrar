const http = require('http');
const app = require('./app');

app.set('port', process.env.PORT || 3000);
const server = http.createServer(app);
// const server = http.createServer((req, res) => {
//     res.end('Voilà la grande réponse du premier serveur !')
// });

server.listen(process.env.PORT || 3000);