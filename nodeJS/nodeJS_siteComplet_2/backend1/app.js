const express = require('express');
const mongoose = require('mongoose');
const Product = require('./models/product');

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

  // récupère tous les enregistrements mongoDb et les envois par json
app.get('/api/products', (req, res, next) => {
  Product.find()
  .then(product => res.status(200).json({"products": product}))
  .catch(error => res.status(404).json({ error }));

});

  // récupère un ID et envois son equivalent mongoDb par json
app.get('/api/products/:id', (req, res, next) => {
  Product.findOne({ _id: req.params.id })
  .then(product => res.status(200).json({"product": product}))
  .catch(error => res.status(404).json({ error }));
});

// récupère le Json d'un objet, l'instancie, crée l'enregistrement dans mongoDb, puis retourne le json de l'instance
app.post('/api/products', (req, res, next) => {
  const product = new Product({
    ...req.body
  });
  product.save()
    .then((product) => res.status(201).json({ "product": product }))
    .catch(error => res.status(400).json({ error }));
});

  // récupère un ID et une req json, update l'élément ciblé sur MongoDb
app.put('/api/products/:id', (req, res, next) => {
  Product.updateOne({ _id: req.params.id }, 
    { ...req.body, _id: req.params.id })
    .then((data) => res.status(200).json({ message: data}))
    .catch(error => res.status(400).json({ error })); 
  });

  // récupère un ID et supprime l'élément ciblé sur MongoDb
  app.delete('/api/products/:id', (req, res, next) => {
    Product.deleteOne({ _id: req.params.id })
      .then(() => res.status(200).json({ message: "Deleted!"}))
      .catch(error => res.status(400).json({ error }));
  });

module.exports = app;