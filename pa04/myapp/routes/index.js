var express = require('express');
var router = express.Router();
var mongoose = require('mongoose');

mongoose.connect(process.env.MONGODB_URI);

var Schema = mongoose.Schema;

var transactionSchema = Schema({
  description: String,
  amount: Number,
  category: String,
  date: Date
});

var transactionItem = mongoose.model('Transactionitem', transactionSchema);

/* GET home page. */
router.get('/', function(req, res, next) {
  var transactions = transactionItem.find();

  res.render('index', {
    title: 'Transaction Application',
    transaction: transactions 
  });
});

router.post('/', function(req, res, next) {
  var transaction = new transactionItem({
    description: req.body.description,
    category: req.body.category,
    amount: req.body.amount,
    date: req.body.date
  });
  transaction.save();
  res.redirect('/');
});


module.exports = router;
