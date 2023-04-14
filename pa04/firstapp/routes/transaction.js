/*
  transaction.js -- Router for the Transaction
  
  Author: Eric Wang
*/
const express = require('express');
const router = express.Router();
const transactionItem = require('../models/transactionItem')
const User = require('../models/User')


/*
this is a very simple server which maintains a key/value
store using an object where the keys and values are lists of strings

*/

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
  async (req, res, next) => {
      let results =
            await transactionItem.aggregate(
                [ 
                  {$group:{
                    _id:'$userId',
                    total:{$count:{}}
                    }},
                  {$sort:{total:-1}},              
                ])
              
        results = 
           await User.populate(results,
                   {path:'_id',
                   select:['description','amount','category','date']})
        // res.json(results)
        res.render('transaction',{results})
});

/*
Author: Eric Wang

Adds a transaction to DB
*/
router.post('/transaction/add_transaction/:transactionId',
  isLoggedIn,
  async (req, res, next) => {
      const transaction = new transactionItem(
        {description:req.body.description,
         category:req.body.category,
         amount:req.body.amount,
         date:req.body.date,
         userId:req.user._id
        })
      await transaction.save();
      res.redirect('/transaction')
});

/*
Author: Eric Wang

Deletes selected transaction from DB
*/
router.get('/transaction/remove/:transactionId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /transaction/remove/:transactionId")
      await transactionItem.deleteOne({_id:req.params.transactionId});
      res.redirect('/transaction')
});

module.exports = router;