var express = require('express');
var router = express.Router();

var mongoose = require('mongoose');

mongoose.connect('mongodb+srv://blacy:4dvSEYSs8j$Rl0b&@wxveshack-db.yrr7y.mongodb.net/?retryWrites=true&w=majority');

var Schema = mongoose.Schema;

var transactionSchema = Schema({
  description: String,
  amount: Number,
  category: String,
  date: Date
});

var TransactionItem = mongoose.model('transactionItem', transactionSchema);

/* GET home page. */
router.get('/', function(req, res, next) {
  TransactionItem.find()
    .then(function(doc) {
      res.render('index', {transactions: doc});
    });
});

router.post('/', function(req, res, next) {
  var transaction = new TransactionItem({
    description: req.body.description,
    category: req.body.category,
    amount: req.body.amount,
    date: req.body.date
  });
  transaction.save();
  res.redirect('/');
});


module.exports = router;
