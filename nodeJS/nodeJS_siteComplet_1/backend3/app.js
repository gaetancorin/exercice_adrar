const express = require('express');
const mongoose = require('mongoose');
const Thing = require('./models/thing');

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

// recoit une requête get avec un ID en parametre dans l'url, récupère le bon élément dans MongoDb et envois l'élément en réponse
app.get('/api/stuff/:id', (req, res, next) => {
  Thing.findOne({ _id: req.params.id })
    .then(thing => res.status(200).json(thing))
    .catch(error => res.status(404).json({ error }));
});

// recoit une requête, récupère tous les éléments dans mongoDb et envois les éléments en réponse.
app.get('/api/stuff', (req, res, next) => {
  Thing.find()
    .then(things => res.status(200).json((things)))
    .catch(error => res.status(400).json({ error }));    
});

//recoit un thing par post que l'on insert dans MongoDb et rand une réponse. On évite les erreurs d'ID en supprimant ce paramètre puisque mongoDb le recrée par défault.
app.post('/api/stuff', (req, res, next) => {
  delete req.body._id;
  const thing = new Thing({
    ...req.body
  });
  thing.save()
    .then(() => res.status(201).json({ message: 'Objet enregistré !'}))
    .catch(error => res.status(400).json({ error }));
});

// recoit une requête put avec un ID en parametre dans l'url, cherche dans MongoDb un élément avec le même ID, puis le modifie avec les nouveaux éléments en vérifiant a nouveau l'ID. 
app.put('/api/stuff/:id', (req, res, next) => {
  Thing.updateOne({ _id: req.params.id }, 
  { ...req.body, _id: req.params.id })
  .then(() => res.status(200).json({ message: 'Objet modifié !'}))
  .catch(error => res.status(400).json({ error })); 
})

// recoit une requête delete avec un ID en parametre dans l'url, cherche dans MongoDb un élément avec le même ID, puis le supprime
app.delete('/api/stuff/:id', (req, res, next) => {
  Thing.deleteOne({ _id: req.params.id })
    .then(() => res.status(200).json({ message: 'Objet supprimé !'}))
    .catch(error => res.status(400).json({ error }));
});

// Si aucun endpoint n'est déclenché, envois une response d'un message par défault. 
app.use((req, res) => {
    res.json({ message: 'Aucun middleware ne correspond a votre url !' }); 
 });

module.exports = app;