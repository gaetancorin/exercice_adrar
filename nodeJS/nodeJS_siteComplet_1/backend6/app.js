const express = require('express');
const mongoose = require('mongoose');

const stuffRoutes = require('./routes/stuff')
const userRoutes = require('./routes/user');

// connection a mongoDB
mongoose.connect('mongodb+srv://gaetan:1234@cluster0.wxcxg.mongodb.net/?retryWrites=true&w=majority',
  { useNewUrlParser: true,
    useUnifiedTopology: true })
  .then(() => console.log('Connexion à MongoDB réussie !'))
  .catch(() => console.log('Connexion à MongoDB échouée !'));

const app = express();
app.use(express.json());

// resoud le problème des CORS lors de la connection a des accès différent
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content, Accept, Content-Type, Authorization');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH, OPTIONS');
    next();
  });

app.use('/api/stuff', stuffRoutes);
app.use('/api/auth', userRoutes);


// Si aucun endpoint n'est déclenché, envois une response d'un message par défault. 
app.use((req, res) => {
    res.json({ message: 'Aucun middleware ne correspond à votre url !' }); 
 });

module.exports = app;