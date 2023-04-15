/*
  transaction.js -- Router for the Transaction
  
  Author: Eric Wang
*/
const express = require('express');
const router = express.Router();
const transactionItem = require('../models/transactionItem')
const User = require('../models/User');

isLoggedIn = (req,res,next) => {
  if (res.locals.loggedIn) {
    next()
  } else {
    res.redirect('/login')
  }
}

/*
Author: Eric Wang

Brings up the transaction page
*/
router.get('/transaction',
  isLoggedIn,
  async(req, res, next) => {
    let results = await transactionItem.find().sort({ date: -1 }).exec();
      res.render('transaction', { results });
    }
  )

/*
Author: Eric Wang

Adds a transaction to DB
*/
router.post('/transaction',
  isLoggedIn,
  async (req, res, next) => {
      const trans = new transactionItem(
        {description:req.body.description,
         category:req.body.category,
         amount:req.body.amount,
         date:req.body.date,
         transactionId:req.transactionId,
         userId:req.userId
        }) 
      await trans.save();
      res.redirect('/transaction');
});

/*
Author: Eric Wang

Deletes selected transaction from DB
*/
router.get('/transaction/delete_transaction/:transactionId',
  isLoggedIn,
  async(req,res,next) => {
    await transactionItem.findByIdAndDelete(req.params.transactionId);
    res.redirect('/transaction')
  });

module.exports = router