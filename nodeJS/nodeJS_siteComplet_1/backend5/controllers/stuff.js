const Thing = require('../models/thing')

//recoit un thing par post que l'on ajoute à MongoDb et rand une réponse. On supprime le paramètre ID puisque mongoDb le recrée par défault(risque d'erreur).
exports.createThing = (req, res, next) => {
    delete req.body._id;
    const thing = new Thing({
        ...req.body
    });
    thing.save()
        .then(() => res.status(201).json({ message: 'Objet enregistré !'}))
        .catch(error => res.status(400).json({ error }));
    }

// recoit une requête put avec un ID en parametre dans l'url, cherche dans MongoDb un élément avec le même ID, puis le modifie avec les nouveaux éléments en vérifiant à nouveau l'ID. 
exports.modifyThing = (req, res, next) => {
    Thing.updateOne({ _id: req.params.id }, 
    { ...req.body, _id: req.params.id })
    .then(() => res.status(200).json({ message: 'Objet modifié !'}))
    .catch(error => res.status(400).json({ error })); 
    }

// recoit une requête delete avec un ID en parametre dans l'url, cherche dans MongoDb un élément avec le même ID, puis le supprime
exports.deleteThing = (req, res, next) => {
    Thing.deleteOne({ _id: req.params.id })
        .then(() => res.status(200).json({ message: 'Objet supprimé !'}))
        .catch(error => res.status(400).json({ error }));
    }
// recoit une requête get avec un ID en parametre dans l'url, récupère le bon élément dans MongoDb et envois l'élément en réponse
exports.getOneThing = (req, res, next) => {
    Thing.findOne({ _id: req.params.id })
      .then(thing => res.status(200).json(thing))
      .catch(error => res.status(404).json({ error }));
  }

// recoit une requête, récupère tous les éléments dans mongoDb et envois les éléments en réponse.
exports.getAllThings = (req, res, next) => {
    Thing.find()
        .then(things => res.status(200).json((things)))
        .catch(error => res.status(400).json({ error }));    
    }