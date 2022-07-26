const Thing = require('../models/thing')
const fs = require('fs');

//recoit par post et en json un thing contenant un str de toute la donnée de l'objet et un file contenant l image. On supprime le paramètre ID puisque mongoDb le recrée par défault, et userId car on prefere utiliser l'information du token pour des raisons de sécurité.
exports.createThing = (req, res, next) => {
    const thingObject = JSON.parse(req.body.thing);
    delete thingObject._id;
    delete thingObject._userId;
    const thing = new Thing({
        ...thingObject,
        userId: req.auth.userId,
        imageUrl: `${req.protocol}://${req.get('host')}/images/${req.file.filename}`
    });
  
    thing.save()
    .then(() => { res.status(201).json({message: 'Objet enregistré !'})})
    .catch(error => { res.status(400).json( { error })})
    }

// On vérifie si on recoit par put et en json un file contenant l 'image.
// Si oui, alors on a recu un objet json "thing" contenant un str de toute la donnée de l'objet a modifier et un objet json "file" contenant l image envoyé. On parse donc le str et le transforme en json, puis on crée un objet "imageUrl" avec l'url de l'image envoyé créée par multer.
// Si non, alors on a recu un objet json contenant directement la donnée de l'objet à modifier. on recupère donc juste la donnée.
// ensuite, on supprime "_userId" au cas ou quelqu'un voudrait changer le propriétaire de l'objet
// Par la suite, on récupère l'objet par le paramètre ID passé en url, on vérifie le token et on modifie notre objet
exports.modifyThing = (req, res, next) => {
    const thingObject = req.file ? {
        ...JSON.parse(req.body.thing),
        imageUrl: `${req.protocol}://${req.get('host')}/images/${req.file.filename}`
    } : { ...req.body };
  
    delete thingObject._userId;
    Thing.findOne({_id: req.params.id})
        .then((thing) => {
            if (thing.userId != req.auth.userId) {
                res.status(401).json({ message : 'Not authorized'});
            } else {
                Thing.updateOne({ _id: req.params.id}, { ...thingObject, _id: req.params.id})
                .then(() => res.status(200).json({message : 'Objet modifié!'}))
                .catch(error => res.status(401).json({ error }));
            }
        })
        .catch((error) => {
            res.status(400).json({ error });
        });
 };

// recoit une requête delete avec un ID dans l'url, si l'userId de l'objet est le meme que le token, on recupère le nom de l'image grace a son attribut dans thing et on supprime l'image avec la fonction asynchrone fs.unlink. Puis on supprime l'enregistrement dans mongoDb.
exports.deleteThing = (req, res, next) => {
    Thing.findOne({ _id: req.params.id})
        .then(thing => {
            if (thing.userId != req.auth.userId) {
                res.status(401).json({message: 'Not authorized'});
            } else {
                const filename = thing.imageUrl.split('/images/')[1];
                fs.unlink(`images/${filename}`, () => {
                    Thing.deleteOne({_id: req.params.id})
                        .then(() => { res.status(200).json({message: 'Objet supprimé !'})})
                        .catch(error => res.status(401).json({ error }));
                });
            }
        })
        .catch( error => {
            res.status(500).json({ error });
        });
 };
// recoit une requête get avec un ID dans l'url, récupère le bon élément dans MongoDb et envois l'élément en réponse
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