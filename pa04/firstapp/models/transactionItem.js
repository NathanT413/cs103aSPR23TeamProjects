// Author: Eric Wang

'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var transactionSchema = Schema( {
  description: String,
  amount: Number,
  category: String,
  date: Date,
  transactionId: {type:ObjectId, ref:'transaction'},
  userId: {type:ObjectId, ref:'user'}
});

module.exports = mongoose.model( 'TransactionItem', transactionSchema);
