/*
  transaction.js -- Router for the Transaction
  
  Author: Eric Wang
*/
const express = require('express');
const router = express.Router();
const Transactions = require('../models/Transaction')
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
            await Transactions.aggregate(
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

Deletes selected transaction from DB
*/
router.get('/transaction/remove/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /todo/remove/:itemId")
      await ToDoItem.deleteOne({_id:req.params.itemId});
      res.redirect('/transaction')
});

/*
Author: Eric Wang

Brings up edit_transaction page
*/
router.get('/todo/edit/:itemId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /todo/edit/:itemId")
      const item = 
       await ToDoItem.findById(req.params.itemId);
      //res.render('edit', { item });
      res.locals.item = item
      res.render('edit_transaction')
      //res.json(item)
});


module.exports = router;